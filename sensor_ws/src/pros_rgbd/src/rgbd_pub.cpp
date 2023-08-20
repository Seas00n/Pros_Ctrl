#include <ros/ros.h>
#include <depthai/depthai.hpp>
#include <cv_bridge/cv_bridge.h>
#include <sensor_msgs/CameraInfo.h>
#include <image_transport/image_transport.h>
#include <chrono>
#include <thread>

sensor_msgs::CameraInfo getCameraInfo(void){
    sensor_msgs::CameraInfo cam;

    std::vector<double> D{0.1133, -0.14896, -0.00208, 0.00356, 0.0};

    boost::array<double, 9> K = {
        859.4891428855528, 0.0, 647.7453, 0.0, 860.4113, 289.1867, 0.0, 0.0, 1.0
    };
    
     boost::array<double, 12> P = {
        873.94275, 0.0, 652.7966, 0.0, 0.0, 879.7893, 287.31157, 0.0, 0.0, 0.0, 1.0, 0.0
    };
    boost::array<double, 9> r = {1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0};

    cam.height = 72;
    cam.width = 1280;
    cam.distortion_model = "plumb_bob";
    cam.D = D;
    cam.K = K;
    cam.P = P;
    cam.R = r;
    cam.binning_x = 0;
    cam.binning_y = 0;
    cam.header.frame_id = "oak_left_camera_optical_frame";  //frame_id为camera，也就是相机名字
    cam.header.stamp = ros::Time::now();
    cam.header.stamp.nsec = 0;
    return cam;
}


int main(int argc, char **argv){
    dai::Pipeline pipeline;
    auto camRgb = pipeline.create<dai::node::ColorCamera>();
    auto xoutRgb = pipeline.create<dai::node::XLinkOut>();
    xoutRgb->setStreamName("rgb");
    camRgb->setPreviewSize(500, 500);
    camRgb->setBoardSocket(dai::CameraBoardSocket::RGB);
    camRgb->setResolution(dai::ColorCameraProperties::SensorResolution::THE_1080_P);
    camRgb->setInterleaved(false);
    camRgb->setColorOrder(dai::ColorCameraProperties::ColorOrder::RGB);
    camRgb->preview.link(xoutRgb->input);
    dai::Device device(pipeline, dai::UsbSpeed::SUPER);
    auto qRgb = device.getOutputQueue("rgb", 4, false);
    ros::init(argc,argv,"cam_node");
    ros::NodeHandle nh;
    image_transport::ImageTransport it(nh);
    image_transport::Publisher pub = it.advertise("camera/image_raw", 10);//发布消息需要使用image_transport
    ros::Publisher info_pub  = nh.advertise<sensor_msgs::CameraInfo>("/camera/camera_info",10);
    sensor_msgs::CameraInfo camera_info_msg;


    int video_device = 1;
    int frame_rate = 25;
    nh.param<int>("video_device", video_device, 0);
    nh.param<int>("frame_rate", frame_rate, 30);
    ros::Rate loop_rate(frame_rate);
    while(nh.ok()){
        cv::Mat image;
        auto inRgb = qRgb->get<dai::ImgFrame>();
        image = inRgb->getCvFrame();
        cv::imshow("rgb",image);
        sensor_msgs::ImagePtr out_msg = cv_bridge::CvImage(std_msgs::Header(), "bgr8", image).toImageMsg();//需要把opencv图片转换为sensor_msgs
        camera_info_msg = getCameraInfo();
        pub.publish(out_msg);
        info_pub.publish(camera_info_msg);
        int key = cv::waitKey(1);
        if(key == 'q'){
            break;
        }
        loop_rate.sleep();

        // std::this_thread::sleep_for(std::chrono::milliseconds(200));
    }
    device.close();
    return 0;
}