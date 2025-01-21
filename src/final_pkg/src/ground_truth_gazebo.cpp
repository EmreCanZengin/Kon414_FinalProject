#include <ros/ros.h>
#include <nav_msgs/Odometry.h>
#include <geometry_msgs/PoseStamped.h>
#include <gazebo_msgs/GetModelState.h>

ros::Publisher pose_pub;
ros::ServiceClient client;

void odometryCallback(const nav_msgs::Odometry::ConstPtr& msg) {
    geometry_msgs::PoseStamped pose_msg;
    pose_msg.header = msg->header;
    pose_msg.pose = msg->pose.pose;

    // Get ground truth from Gazebo
    gazebo_msgs::GetModelState srv;
    srv.request.model_name = "turtlebot3";
    srv.request.relative_entity_name = "office_geometry";
    if (client.call(srv)) {
        pose_msg.pose = srv.response.pose;
    } else {
        ROS_ERROR("Failed to call service gazebo/get_model_state");
    }

    pose_pub.publish(pose_msg);
}

int main(int argc, char** argv) {
    ros::init(argc, argv, "ground_truth_publisher");
    ros::NodeHandle nh;

    pose_pub = nh.advertise<geometry_msgs::PoseStamped>("/ground_truth", 10);
    ros::Subscriber odom_sub = nh.subscribe("/odom", 10, odometryCallback);

    client = nh.serviceClient<gazebo_msgs::GetModelState>("gazebo/get_model_state");

    ROS_INFO("Wait for service ....");
    ros::service::waitForService("gazebo/get_model_state", -1);
    ROS_INFO("... Got it!");

    ros::spin();
    return 0;
}
