# C++实现facenet提取特征
## 先放参考链接
首先，致敬[facenet原作](https://github.com/davidsandberg/facenet)；  
其次，感谢[tensorflow](https://github.com/tensorflow/tensorflow)  
还有参考的csdn上的一些链接：【忘记保存了，太多了。。。】。   
特别参考：[tensorflow-example](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/examples/label_image)
## 介绍
因为facenet用了triplet loss进行训练，在lfw上的准确率达到了99.4%，在我们自己的库上也到了94%，所以我们准备把facenet提取的特征部署上。
关于facenet在lfw上的测试可以参考[FaceNet人脸识别网络的应用](https://github.com/alfredtorres/Reading-notebook/blob/master/Experiment/FaceNet_Validate_on_lfw.md#facenet%E4%BA%BA%E8%84%B8%E8%AF%86%E5%88%AB%E7%BD%91%E7%BB%9C%E7%9A%84%E5%BA%94%E7%94%A8)
,在用c++实现之前请先阅读facnet的源码，以及在python上多跑一跑。
## 工程配置
关于编译tensorflow请参考[编译TensorFlow C/C++接口](https://github.com/alfredtorres/Reading-notebook/blob/master/Experiment/TensorFlow%E7%BC%96%E8%AF%91.md)
最终要编译出`tensorflow.dll`和`tensorflow.lib`，需要用  
### 1 属性配置
在属性管理器的VC++目录的包含目录添加：
```
D:\tensorflow-r1.7
D:\tensorflow-r1.7\tensorflow\contrib\cmake\build
D:\tensorflow-r1.7\tensorflow\contrib\cmake\build\protobuf\src\protobuf\src
D:\tensorflow-r1.7\tensorflow\contrib\cmake\build\external\nsync\public
D:\tensorflow-r1.7\tensorflow\contrib\cmake\build\Release
D:\tensorflow-r1.7\tensorflow\contrib\cmake\build\external\eigen_archive
```
在项目添加tensorflow.lib，在编译出的x64文件夹下放tensorflow.dll  
新建一个头文件.h，加入下面两句话
```
#define COMPILER_MSVC
#define NOMINMAX
```
参考example里的image_label文件新建一个.cpp文件
```
static Status ReadEntireFile(tensorflow::Env* env, const string& filename,
	Tensor* output) {
	tensorflow::uint64 file_size = 0;
	TF_RETURN_IF_ERROR(env->GetFileSize(filename, &file_size));

	string contents;
	contents.resize(file_size);

	std::unique_ptr<tensorflow::RandomAccessFile> file;
	TF_RETURN_IF_ERROR(env->NewRandomAccessFile(filename, &file));

	tensorflow::StringPiece data;
	TF_RETURN_IF_ERROR(file->Read(0, file_size, &data, &(contents)[0]));
	if (data.size() != file_size) {
		return tensorflow::errors::DataLoss("Truncated read of '", filename,
			"' expected ", file_size, " got ",
			data.size());
	}
	output->scalar<string>()() = data.ToString();
	return Status::OK();
}

// Reads a model graph definition from disk, and creates a session object you
// can use to run it.
Status LoadGraph(const string& graph_file_name,
	std::unique_ptr<tensorflow::Session>* session) {
	tensorflow::GraphDef graph_def;
	Status load_graph_status =
		ReadBinaryProto(tensorflow::Env::Default(), graph_file_name, &graph_def);
	if (!load_graph_status.ok()) {
		return tensorflow::errors::NotFound("Failed to load compute graph at '",
			graph_file_name, "'");
	}
	session->reset(tensorflow::NewSession(tensorflow::SessionOptions()));
	Status session_create_status = (*session)->Create(graph_def);
	if (!session_create_status.ok()) {
		return session_create_status;
	}
	return session_create_status;
}
// Given an image file name, read in the data, try to decode it as an image,
// resize it to the requested size, and then scale the values as desired.
Status ReadTensorFromImageFile(const string& file_name, const int input_height,
	const int input_width, const float input_mean,
	const float input_std,
	std::vector<Tensor>* out_tensors) {
	auto root = tensorflow::Scope::NewRootScope();
	using namespace ::tensorflow::ops;  // NOLINT(build/namespaces)

	string input_name = "file_reader";
	string output_name = "normalized";

	// read file_name into a tensor named input
	Tensor input(tensorflow::DT_STRING, tensorflow::TensorShape());
	TF_RETURN_IF_ERROR(
		ReadEntireFile(tensorflow::Env::Default(), file_name, &input));

	// use a placeholder to read input data
	auto file_reader =
		Placeholder(root.WithOpName("input"), tensorflow::DataType::DT_STRING);

	std::vector<std::pair<string, tensorflow::Tensor>> inputs = {
		{ "input", input },
	};

	// Now try to figure out what kind of file it is and decode it.
	const int wanted_channels = 3;
	tensorflow::Output image_reader;
	if (tensorflow::StringPiece(file_name).ends_with(".png")) {
		image_reader = DecodePng(root.WithOpName("png_reader"), file_reader,
			DecodePng::Channels(wanted_channels));
	}
	else if (tensorflow::StringPiece(file_name).ends_with(".gif")) {
		// gif decoder returns 4-D tensor, remove the first dim
		image_reader =
			Squeeze(root.WithOpName("squeeze_first_dim"),
				DecodeGif(root.WithOpName("gif_reader"), file_reader));
	}
	else if (tensorflow::StringPiece(file_name).ends_with(".bmp")) {
		image_reader = DecodeBmp(root.WithOpName("bmp_reader"), file_reader);
	}
	else {
		// Assume if it's neither a PNG nor a GIF then it must be a JPEG.
		image_reader = DecodeJpeg(root.WithOpName("jpeg_reader"), file_reader,
			DecodeJpeg::Channels(wanted_channels));
	}
	// Now cast the image data to float so we can do normal math on it.
	auto float_caster =
		Cast(root.WithOpName("float_caster"), image_reader, tensorflow::DT_FLOAT);
	// The convention for image ops in TensorFlow is that all images are expected
	// to be in batches, so that they're four-dimensional arrays with indices of
	// [batch, height, width, channel]. Because we only have a single image, we
	// have to add a batch dimension of 1 to the start with ExpandDims().
	auto dims_expander = ExpandDims(root, float_caster, 0);
	// Bilinearly resize the image to fit the required dimensions.
	auto resized = ResizeBilinear(
		root, dims_expander,
		Const(root.WithOpName("size"), { input_height, input_width }));
	// Subtract the mean and divide by the scale.
	Div(root.WithOpName(output_name), Sub(root, resized, { input_mean }),
	{ input_std });

	// This runs the GraphDef network definition that we've just constructed, and
	// returns the results in the output tensor.
	tensorflow::GraphDef graph;
	TF_RETURN_IF_ERROR(root.ToGraphDef(&graph));

	std::unique_ptr<tensorflow::Session> session(
		tensorflow::NewSession(tensorflow::SessionOptions()));
	TF_RETURN_IF_ERROR(session->Create(graph));
	TF_RETURN_IF_ERROR(session->Run({ inputs }, { output_name }, {}, out_tensors));
	return Status::OK();
}

// 主函数由于某种原因不能放，大家参考example里的例子吧，如果tensorflow版本不同，去查看对应的版本，有些函数会改
```
