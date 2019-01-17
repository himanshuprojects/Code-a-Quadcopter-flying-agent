import pandas as pd
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def to_original(episode_pose,epi,axes):
    x=episode_pose[epi][axes]
    x=x.strip('[')
    x=x.strip(']')
    l=list(x.split(","))
    lx=[]
    for i in l:
        lx.append(float(i))
    return lx

def plot3d(ax,x, y, z, **kwargs):
    ax.scatter([x], [y], [z], **kwargs)
    ax.text(x, y, z, "({:.1f}, {:.1f}, {:.1f})".format(x, y, z), ha = 'right')
    
def ploting_start(ax,plt,x,y,z,target_pos):
    ax.plot(x,y,z)

   
    t_x,t_y,t_z=target_pos[:3]

    i_x=x[0]
    i_y=y[0]
    i_z=z[0]

    l_x=x[len(x)-1]
    l_y=y[len(y)-1]
    l_z=z[len(z)-1]

    m_x=x[int(len(x)/2)]
    m_y=y[int(len(y)/2)]
    m_z=z[int(len(z)/2)]

    plot3d(ax,l_x,l_y,l_z, c='y', marker='*', s=100, label='episode_end_pos')
    plot3d(ax,i_x,i_y,i_z, c='b', marker='o', s=50, label='start_pos')
    plot3d(ax,t_x,t_y,t_z, c='r', marker='o', s=50, label='actual_end_pos')
    #plot3d(ax,m_x,m_y,m_z, c='g', marker='o', s=50, label='middle_pos')

    ax.set_xlabel('x-axis')
    ax.set_ylabel('y-axis')
    ax.set_zlabel('z-axis')

    
def trace_path(episode_pose,epi,target_pos):
    
    

    fig = plt.figure(figsize=(20,5)) 
    
    ax1=fig.add_subplot(1,4,1,projection='3d')
    x=to_original(episode_pose,epi[0],'x')
    y=to_original(episode_pose,epi[0],'y')
    z=to_original(episode_pose,epi[0],'z')
    ploting_start(ax1,plt,x,y,z,target_pos)
    ax1.set_title("Drone path in {0} episode".format(epi[0]))

    ax2=fig.add_subplot(1,4,2,projection='3d')
    x=to_original(episode_pose,epi[1],'x')
    y=to_original(episode_pose,epi[1],'y')
    z=to_original(episode_pose,epi[1],'z')
    ploting_start(ax2,plt,x,y,z,target_pos)
    ax2.set_title("Drone path in {0} episode".format(epi[1]))

    ax3=fig.add_subplot(1,4,3,projection='3d')
    x=to_original(episode_pose,epi[2],'x')
    y=to_original(episode_pose,epi[2],'y')
    z=to_original(episode_pose,epi[2],'z')
    ploting_start(ax3,plt,x,y,z,target_pos)
    ax3.set_title("Drone path in {0} episode".format(epi[2]))

    ax4=fig.add_subplot(1,4,4,projection='3d')
    x=to_original(episode_pose,epi[3],'x')
    y=to_original(episode_pose,epi[3],'y')
    z=to_original(episode_pose,epi[3],'z')
    ploting_start(ax4,plt,x,y,z,target_pos)
    ax4.set_title("Drone path in {0} episode".format(epi[3]))
    plt.legend()    
    plt.show()
    

#visualize how the position of the quadcopter evolved during the simulation.    
def position2d(results):
    plt.plot(results['time'], results['x'], label='x')
    plt.plot(results['time'], results['y'], label='y')
    plt.plot(results['time'], results['z'], label='z')
    plt.legend()
    _ = plt.ylim()
   
#visualize the velocity of the quadcopter
def velocity2d(results):
    plt.plot(results['time'], results['x_velocity'], label='x_hat')
    plt.plot(results['time'], results['y_velocity'], label='y_hat')
    plt.plot(results['time'], results['z_velocity'], label='z_hat')
    plt.legend()
    _ = plt.ylim()
    
#Euler angles (the rotation of the quadcopter over the 𝑥-, 𝑦-, and 𝑧-axes)
def eular_angle2d(results):
    plt.plot(results['time'], results['phi'], label='phi')
    plt.plot(results['time'], results['theta'], label='theta')
    plt.plot(results['time'], results['psi'], label='psi')
    plt.legend()
    _ = plt.ylim()
    
#before plotting the velocities (in radians per second) corresponding to each of the Euler angles.
def eular_velocity2d(results):
    plt.plot(results['time'], results['phi_velocity'], label='phi_velocity')
    plt.plot(results['time'], results['theta_velocity'], label='theta_velocity')
    plt.plot(results['time'], results['psi_velocity'], label='psi_velocity')
    plt.legend()
    _ = plt.ylim()