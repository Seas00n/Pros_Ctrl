#include <ros/ros.h>
#include <depthai/depthai.hpp>
#include <cv_bridge/cv_bridge.h>
#include <sensor_msgs/CameraInfo.h>
#include <image_transport/image_transport.h>

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
    image_transport::Publisher pub = it.advertise("rgbd_pub/image_raw", 10);//发布消息需要使用image_transport
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
        pub.publish(out_msg);
        int key = cv::waitKey(1);
        if(key == 'q'){
            break;
        }
        loop_rate.sleep();
    }
    device.close();
    return 0;
}