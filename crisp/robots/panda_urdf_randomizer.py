# Helper function returning a customized URDF of the 1R planar manipulator
import numpy as np


def generate_custom_urdf(joint_ang_bias: tuple = (0, 0, 0, 0, 0, 0, 0),
                         joint_pos_bias: tuple = ((0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),
                                                      (0,0,0),(0,0,0),(0,0,0),(0,0,0))) -> str:

    robot_urdf = \
f"""<?xml version="1.0" ?>
<!-- =================================================================================== -->
<!-- |    This document was autogenerated by xacro from panda_arm_hand.urdf.xacro      | -->
<!-- |    EDITING THIS FILE BY HAND IS NOT RECOMMENDED                                 | -->
<!-- =================================================================================== -->
<robot name="panda" xmlns:xacro="http://www.ros.org/wiki/xacro">
  <link name="panda_link0">
    <inertial>
      <origin rpy="0 0 0" xyz="0 0 0.05"/>
       <mass value="2.9"/>
       <inertia ixx="0.1" ixy="0" ixz="0" iyy="0.1" iyz="0" izz="0.1"/>
    </inertial>
    <visual>
      <geometry>
        <mesh filename="package://meshes/collision/link0.obj"/>
      </geometry>
      <material name="panda_white">
            <color rgba="1. 1. 1. 1."/>
        </material>
    </visual>
    <collision>
      <geometry>
        <mesh filename="package://meshes/collision/link0.obj"/>
      </geometry>
      <material name="panda_white"/>
    </collision>
  </link>
  <joint name="panda_joint1" type="revolute">
    <safety_controller k_position="100.0" k_velocity="40.0" soft_lower_limit="-2.8973" soft_upper_limit="2.8973"/>
    <origin rpy="0 0 0" xyz="{joint_pos_bias[0][0]} {joint_pos_bias[0][1]} {0.333 + joint_pos_bias[0][2]}"/>
    <parent link="panda_link0"/>
    <child link="panda_link1"/>
    <axis xyz="0 0 1"/>
    <limit effort="87" lower="-2.9671" upper="2.9671" velocity="2.1750"/>
  </joint>
  <link name="panda_link1">
    <inertial>
      <origin rpy="0 0 0" xyz="0 -0.04 -0.05"/>
       <mass value="2.7"/>
       <inertia ixx="0.1" ixy="0" ixz="0" iyy="0.1" iyz="0" izz="0.1"/>
    </inertial>
    <visual>
      <origin rpy="0 0 {joint_ang_bias[0]}" xyz = "0 0 0" />
      <geometry>
        <mesh filename="package://meshes/visual/link1.obj"/>
      </geometry>
      <material name="panda_white"/>
    </visual>
    <collision>
      <geometry>
        <mesh filename="package://meshes/collision/link1.obj"/>
      </geometry>
      <material name="panda_white"/>
    </collision>
  </link>
  <joint name="panda_joint2" type="revolute">
    <safety_controller k_position="100.0" k_velocity="40.0" soft_lower_limit="-1.7628" soft_upper_limit="1.7628"/>
    <origin rpy="-1.57079632679 0 {joint_ang_bias[0]}" xyz="{joint_pos_bias[1][0]} {joint_pos_bias[1][1]} {joint_pos_bias[1][2]}"/>
    <parent link="panda_link1"/>
    <child link="panda_link2"/>
    <axis xyz="0 0 1"/>
    <limit effort="87" lower="-1.8326" upper="1.8326" velocity="2.1750"/>
  </joint>
  <link name="panda_link2">
    <inertial>
      <origin rpy="0 0 0" xyz="0 -0.04 0.06"/>
       <mass value="2.73"/>
       <inertia ixx="0.1" ixy="0" ixz="0" iyy="0.1" iyz="0" izz="0.1"/>
    </inertial>
    <visual>
      <origin rpy="0 0 {joint_ang_bias[1]}" xyz = "0 0 0" />
      <geometry>
        <mesh filename="package://meshes/visual/link2.obj"/>
      </geometry>
      <material name="panda_white"/>
    </visual>
    <collision>
      <geometry>
        <mesh filename="package://meshes/collision/link2.obj"/>
      </geometry>
      <material name="panda_white"/>
    </collision>
  </link>
  <joint name="panda_joint3" type="revolute">
    <safety_controller k_position="100.0" k_velocity="40.0" soft_lower_limit="-2.8973" soft_upper_limit="2.8973"/>
    <origin rpy="1.57079632679 0 {joint_ang_bias[1]}" xyz="{0.316 * np.sin(joint_ang_bias[1]) + joint_pos_bias[2][0]} {-0.316 * np.cos(joint_ang_bias[1]) + joint_pos_bias[2][1]} {joint_pos_bias[2][2]}"/>
    <parent link="panda_link2"/>
    <child link="panda_link3"/>
    <axis xyz="0 0 1"/>
    <limit effort="87" lower="-2.9671" upper="2.9671" velocity="2.1750"/>
  </joint>
  <link name="panda_link3">
      <inertial>
      <origin rpy="0 0 0" xyz="0.01 0.01 -0.05"/>
       <mass value="2.04"/>
       <inertia ixx="0.1" ixy="0" ixz="0" iyy="0.1" iyz="0" izz="0.1"/>
    </inertial>
    <visual>
      <origin rpy="0 0 {joint_ang_bias[2]}" xyz = "0 0 0" />
      <geometry>
        <mesh filename="package://meshes/visual/link3.obj"/>
      </geometry>
      <material name="panda_red">
            <color rgba="1. 1. 1. 1."/>
        </material>
    </visual>
    <collision>
      <geometry>
        <mesh filename="package://meshes/collision/link3.obj"/>
      </geometry>
    </collision>
  </link>
  <joint name="panda_joint4" type="revolute">
    <safety_controller k_position="100.0" k_velocity="40.0" soft_lower_limit="-3.0718" soft_upper_limit="-0.0698"/>
    <origin rpy="1.57079632679 0 {joint_ang_bias[2]}" xyz="{0.0825*np.cos(joint_ang_bias[2]) + joint_pos_bias[3][0]} {0.0825*np.sin(joint_ang_bias[2]) + joint_pos_bias[3][1]} {joint_pos_bias[3][2]}"/>
    <parent link="panda_link3"/>
    <child link="panda_link4"/>
    <axis xyz="0 0 1"/>
    <limit effort="87" lower="-3.1416" upper="0.0" velocity="2.1750"/>
  </joint>
  <link name="panda_link4">
    <inertial>
      <origin rpy="0 0 0" xyz="-0.03 0.03 0.02"/>
       <mass value="2.08"/>
       <inertia ixx="0.1" ixy="0" ixz="0" iyy="0.1" iyz="0" izz="0.1"/>
    </inertial>
    <visual>      
      <origin rpy="0 0 {joint_ang_bias[3]}" xyz = "0 0 0" />
      <geometry>
        <mesh filename="package://meshes/visual/link4.obj"/>
      </geometry>
      <material name="panda_white"/>
    </visual>
    <collision>
      <geometry>
        <mesh filename="package://meshes/collision/link4.obj"/>
      </geometry>
      <material name="panda_white"/>
    </collision>
  </link>
  <joint name="panda_joint5" type="revolute">
    <safety_controller k_position="100.0" k_velocity="40.0" soft_lower_limit="-2.8973" soft_upper_limit="2.8973"/>
    <origin rpy="-1.57079632679 0 {joint_ang_bias[3]}" xyz="{-0.0825*np.cos(joint_ang_bias[3])-0.384*np.sin(joint_ang_bias[3]) + joint_pos_bias[4][0]} {-0.0825*np.sin(joint_ang_bias[3])+0.384*np.cos(joint_ang_bias[3]) + joint_pos_bias[4][1]} {joint_pos_bias[4][2]}"/>
    <parent link="panda_link4"/>
    <child link="panda_link5"/>
    <axis xyz="0 0 1"/>
    <limit effort="12" lower="-2.9671" upper="2.9671" velocity="2.6100"/>
  </joint>
  <link name="panda_link5">
    <inertial>
      <origin rpy="0 0 0" xyz="0 0.04 -0.12"/>
       <mass value="3"/>
       <inertia ixx="0.1" ixy="0" ixz="0" iyy="0.1" iyz="0" izz="0.1"/>
    </inertial>
    <visual>
      <origin rpy="0 0 {joint_ang_bias[4]}" xyz = "0 0 0" />
      <geometry>
        <mesh filename="package://meshes/visual/link5.obj"/>
      </geometry>
      <material name="panda_white"/>
    </visual>
    <collision>
      <geometry>
        <mesh filename="package://meshes/collision/link5.obj"/>
      </geometry>
      <material name="panda_white"/>
    </collision>
  </link>
  <joint name="panda_joint6" type="revolute">
    <safety_controller k_position="100.0" k_velocity="40.0" soft_lower_limit="-0.0175" soft_upper_limit="3.7525"/>
    <origin rpy="1.57079632679 0 {joint_ang_bias[4]}" xyz="{joint_pos_bias[5][0]} {joint_pos_bias[5][1]} {joint_pos_bias[5][2]}"/>
    <parent link="panda_link5"/>
    <child link="panda_link6"/>
    <axis xyz="0 0 1"/>
    <limit effort="12" lower="-0.0873" upper="3.8223" velocity="2.6100"/>
  </joint>
  <link name="panda_link6">
    <inertial>
      <origin rpy="0 0 0" xyz="0.04 0 0"/>
       <mass value="1.3"/>
       <inertia ixx="0.1" ixy="0" ixz="0" iyy="0.1" iyz="0" izz="0.1"/>
    </inertial>
    <visual>
      <origin rpy="0 0 {joint_ang_bias[5]}" xyz = "0 0 0" />
      <geometry>
        <mesh filename="package://meshes/visual/link6.obj"/>
      </geometry>
      <material name="panda_white"/>
    </visual>
    <collision>
      <geometry>
        <mesh filename="package://meshes/collision/link6.obj"/>
      </geometry>
      <material name="panda_white"/>
    </collision>
  </link>
  <joint name="panda_joint7" type="revolute">
    <safety_controller k_position="100.0" k_velocity="40.0" soft_lower_limit="-2.8973" soft_upper_limit="2.8973"/>
    <origin rpy="1.57079632679 0 {joint_ang_bias[5]}" xyz="{0.088*np.cos(joint_ang_bias[5]) + joint_pos_bias[6][0]} {0.088*np.sin(joint_ang_bias[5]) + joint_pos_bias[6][1]} {joint_pos_bias[6][2]}"/>
    <parent link="panda_link6"/>
    <child link="panda_link7"/>
    <axis xyz="0 0 1"/>
    <limit effort="12" lower="-2.9671" upper="2.9671" velocity="2.6100"/>
  </joint>
  <link name="panda_link7">
    <inertial>
      <origin rpy="0 0 0" xyz="0 0 0.08"/>
       <mass value=".2"/>
       <inertia ixx="0.1" ixy="0" ixz="0" iyy="0.1" iyz="0" izz="0.1"/>
    </inertial>
    <visual>
      <origin rpy="0 0 {joint_ang_bias[6]}" xyz = "0 0 0" />
      <geometry>
        <mesh filename="package://meshes/collision/link7.obj"/>
      </geometry>
      <material name="panda_white"/>
    </visual>
    <collision>
      <geometry>
        <mesh filename="package://meshes/collision/link7.obj"/>
      </geometry>
      <material name="panda_white"/>
    </collision>
  </link>
  <joint name="panda_joint8" type="fixed">
    <origin rpy="0 0 {joint_ang_bias[6]}" xyz="{joint_pos_bias[7][0]} {joint_pos_bias[7][1]} {0.107 + joint_pos_bias[7][2]}"/>
    <parent link="panda_link7"/>
    <child link="panda_link8"/>
    <axis xyz="0 0 0"/>
  </joint>
  <link name="panda_link8">
     <inertial>
      <origin rpy="0 0 0" xyz="0 0 0"/>
       <mass value="0.0"/>
       <inertia ixx="0.1" ixy="0" ixz="0" iyy="0.1" iyz="0" izz="0.1"/>
    </inertial>
  </link>
  <joint name="panda_hand_joint" type="fixed">
    <parent link="panda_link8"/>
    <child link="panda_hand"/>
    <origin rpy="0 0 -0.785398163397" xyz="{joint_pos_bias[8][0]} {joint_pos_bias[8][1]} {joint_pos_bias[8][2]}"/>
  </joint>
  <link name="panda_hand">
    <inertial>
      <origin rpy="0 0 0" xyz="0 0 0.04"/>
       <mass value=".81"/>
       <inertia ixx="0.1" ixy="0" ixz="0" iyy="0.1" iyz="0" izz="0.1"/>
    </inertial>
    <visual>
      <geometry>
        <mesh filename="package://meshes/visual/hand.obj"/>
      </geometry>
      <material name="panda_white"/>
    </visual>
    <collision>
      <geometry>
        <mesh filename="package://meshes/collision/hand.obj"/>
      </geometry>
      <material name="panda_white"/>
    </collision>
  </link>
  <link name="panda_leftfinger">
       <contact>
      <friction_anchor/>
      <stiffness value="30000.0"/>
      <damping value="1000.0"/>
      <spinning_friction value="0.1"/>
      <lateral_friction value="1.0"/>
    </contact>
    <inertial>
      <origin rpy="0 0 0" xyz="0 0.01 0.02"/>
       <mass value="0.1"/>
       <inertia ixx="0.1" ixy="0" ixz="0" iyy="0.1" iyz="0" izz="0.1"/>
    </inertial>
    <visual>
      <geometry>
        <mesh filename="package://meshes/visual/finger.obj"/>
      </geometry>
      <material name="panda_white"/>
    </visual>
    <collision>
      <geometry>
        <mesh filename="package://meshes/collision/finger.obj"/>
      </geometry>
      <material name="panda_white"/>
    </collision>
  </link>
  <link name="panda_rightfinger">
        <contact>
      <friction_anchor/>
      <stiffness value="30000.0"/>
      <damping value="1000.0"/>
      <spinning_friction value="0.1"/>
      <lateral_friction value="1.0"/>
    </contact>

    <inertial>
      <origin rpy="0 0 0" xyz="0 -0.01 0.02"/>
       <mass value="0.1"/>
       <inertia ixx="0.1" ixy="0" ixz="0" iyy="0.1" iyz="0" izz="0.1"/>
    </inertial>
    <visual>
      <origin rpy="0 0 3.14159265359" xyz="0 0 0"/>
      <geometry>
        <mesh filename="package://meshes/visual/finger.obj"/>
      </geometry>
      <material name="panda_white"/>
    </visual>
    <collision>
      <origin rpy="0 0 3.14159265359" xyz="0 0 0"/>
      <geometry>
        <mesh filename="package://meshes/collision/finger.obj"/>
      </geometry>
      <material name="panda_white"/>
    </collision>
  </link>
  <joint name="panda_finger_joint1" type="prismatic">
    <parent link="panda_hand"/>
    <child link="panda_leftfinger"/>
    <origin rpy="0 0 0" xyz="0 0 0.0584"/>
    <axis xyz="0 1 0"/>
    <limit effort="20" lower="0.0" upper="0.04" velocity="0.2"/>
  </joint>
  <joint name="panda_finger_joint2" type="prismatic">
    <parent link="panda_hand"/>
    <child link="panda_rightfinger"/>
    <origin rpy="0 0 0" xyz="0 0 0.0584"/>
    <axis xyz="0 -1 0"/>
    <limit effort="20" lower="0.0" upper="0.04" velocity="0.2"/>
    <mimic joint="panda_finger_joint1"/>
  </joint>
   <link name="panda_grasptarget">
 <inertial>
      <origin rpy="0 0 0" xyz="0 0 0"/>
       <mass value="0.0"/>
       <inertia ixx="0.1" ixy="0" ixz="0" iyy="0.1" iyz="0" izz="0.1"/>
    </inertial>
   </link>
   <joint name="panda_grasptarget_hand" type="fixed">
    <parent link="panda_hand"/>
    <child link="panda_grasptarget"/>
    <origin rpy="0 0 0" xyz="0 0 0.105"/>
  </joint>
</robot>
    """
    return robot_urdf