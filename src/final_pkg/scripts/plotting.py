import rosbag
import matplotlib.pyplot as plt

# Open the bag file
bag = rosbag.Bag('/home/mrrich/Desktop/Kon414/final_ws/2025-01-20-23-18-36.bag')

# Extract data from a specific topic
topics = {"amcl": {"t": [], "vals": []}, "ground": {"t": [], "vals": []}}
for topic, msg, t in bag.read_messages(topics=['/amcl_pose', "/ground_truth"]):
    if topic == "/amcl_pose":
        topics["amcl"]["t"].append(t.to_sec())
        topics["amcl"]["vals"].append(msg)
    if topic == "/ground_truth":
        topics["ground"]["t"].append(t.to_sec())
        topics["ground"]["vals"].append(msg)

bag.close()

# AMCL positions
amcl_pos_x = [pose_wcov.pose.pose.position.x for pose_wcov in topics["amcl"]["vals"]]
amcl_pos_y = [pose_wcov.pose.pose.position.y for pose_wcov in topics["amcl"]["vals"]]
amcl_pos_z = [pose_wcov.pose.pose.position.z for pose_wcov in topics["amcl"]["vals"]]

# AMCL orientations 
amcl_or_x = [pose_wcov.pose.pose.orientation.x for pose_wcov in topics["amcl"]["vals"]]
amcl_or_y = [pose_wcov.pose.pose.orientation.y for pose_wcov in topics["amcl"]["vals"]]
amcl_or_z = [pose_wcov.pose.pose.orientation.z for pose_wcov in topics["amcl"]["vals"]]

# Ground Truth positions
ground_pos_x = [pose_wcov.pose.position.x for pose_wcov in topics["ground"]["vals"]]
ground_pos_y = [pose_wcov.pose.position.y for pose_wcov in topics["ground"]["vals"]]
ground_pos_z = [pose_wcov.pose.position.z for pose_wcov in topics["ground"]["vals"]]

# Ground Truth orientations 
ground_or_x = [pose_wcov.pose.orientation.x for pose_wcov in topics["ground"]["vals"]]
ground_or_y = [pose_wcov.pose.orientation.y for pose_wcov in topics["ground"]["vals"]]
ground_or_z = [pose_wcov.pose.orientation.z for pose_wcov in topics["ground"]["vals"]]


# Plot the extracted data for both topics
fig, ax = plt.subplots(3, 1, figsize=(10, 6))

# Plot X position
ax[0].plot(topics["amcl"]["t"], amcl_pos_x, label="AMCL X", color='b')
ax[0].plot(topics["ground"]["t"], ground_pos_x, label="Ground Truth X", color='r')
ax[0].set_ylabel('X Position')
ax[0].legend()

# Plot Y position
ax[1].plot(topics["amcl"]["t"], amcl_pos_y, label="AMCL Y", color='b')
ax[1].plot(topics["ground"]["t"], ground_pos_y, label="Ground Truth Y", color='r')
ax[1].set_ylabel('Y Position')
ax[1].legend()

# Plot Z position
ax[2].plot(topics["amcl"]["t"], amcl_pos_z, label="AMCL Z", color='b')
ax[2].plot(topics["ground"]["t"], ground_pos_z, label="Ground Truth Z", color='r')
ax[2].set_ylabel('Z Position')
ax[2].legend()

# Set common labels
plt.xlabel('Time (s)')
plt.tight_layout()

fig_name = "position.png"
plt.savefig(fname=f"../images/{fig_name}", format="png")
plt.close(fig)
# Plot the extracted data for both topics
fig, ax = plt.subplots(3, 1, figsize=(10, 6))

# Plot X position
ax[0].plot(topics["amcl"]["t"], amcl_or_x, label="AMCL X", color='b')
ax[0].plot(topics["ground"]["t"], ground_or_x, label="Ground Truth X", color='r')
ax[0].set_ylabel('X Orientation')
ax[0].legend()

# Plot Y position
ax[1].plot(topics["amcl"]["t"], amcl_or_y, label="AMCL Y", color='b')
ax[1].plot(topics["ground"]["t"], ground_or_y, label="Ground Truth Y", color='r')
ax[1].set_ylabel('Y Orientation')
ax[1].legend()

# Plot Z position
ax[2].plot(topics["amcl"]["t"], amcl_or_z, label="AMCL Z", color='b')
ax[2].plot(topics["ground"]["t"], ground_or_z, label="Ground Truth Z", color='r')
ax[2].set_ylabel('Z Orientation')
ax[2].legend()

# Set common labels
plt.xlabel('Time (s)')
plt.tight_layout()

fig_name = "orientation.png"
plt.savefig(fname=f"../images/{fig_name}", format="png")