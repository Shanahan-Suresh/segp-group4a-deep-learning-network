import os

import numpy
import numpy as np
from PIL import Image, ImageOps
from matplotlib import pyplot as plt
from matplotlib.widgets import Button
from torchvision import transforms

os.environ['KMP_DUPLICATE_LIB_OK']='True'

global button_clicked_count


def format_cursor_data(data):
    if data[0] > 0.45 and data [1] >= 0.45:
        return "[" + str(round((13*data[0] + 8*data[1] + 5.6*data[2]),2)) + "]"
    if data[0] < 0.1 and data[1] >= data[2] :
        if(data[1] - data[2] >= 0.2):
            return "[" + str(round((15*data[0] + 14*data[1] + 5*data[2]),2)) + "]"
        else:
            return "[" + str(round((15*data[0] + 12*data[1] + 4*data[2]),2)) + "]"
    return "[" + str(round((23*data[0] + 10*data[1] + 6*data[2]),2)) + "]"
class LineBuilder(object):
    def __init__(self, fig, ax):
        self.xs = []
        self.ys = []
        self.ax = ax
        self.fig = fig
        self.points = Points()

    def mouse_click(self, event):
        print('click', event)
        if not event.inaxes:
            return
        #left click
        if event.button == 1 and 0 <= event.xdata <= 666 and 0 <= event.ydata <= 500 :

            self.xs.append(event.xdata)
            self.ys.append(event.ydata)
            if len(self.xs) % 2 == 1:
                self.points.x_start_point(event.xdata)
                self.points.y_start_point(event.ydata)
            #add a line to plot if it has 2 points
            if len(self.xs) % 2 == 0:


                self.points.x_end_point(event.xdata)
                self.points.y_end_point(event.ydata)
                line, = self.ax.plot([self.xs[-2], self.xs[-1]], [self.ys[-2], self.ys[-1]], 'r')
                line.figure.canvas.draw()
                fig.canvas.mpl_disconnect(cid1)
                fig.canvas.mpl_disconnect(cid2)

        #right click
        if event.button == 3:
            if len(self.xs) > 0:
                self.xs.pop()
                self.ys.pop()
            #delete last line drawn if the line is missing a point,
            #never delete the original stock plot
            if len(self.xs) % 2 == 1 and len(self.ax.lines) > 1:
                self.ax.lines.pop()
                fig.canvas.mpl_disconnect(cid1)
                fig.canvas.mpl_disconnect(cid2)
            #refresh plot
            self.fig.canvas.draw()

    def mouse_move(self, event):
        if not event.inaxes:
            return
        #dtaw a temporary line from a single point to the mouse position
        #delete the temporary line when mouse move to another position
        if len(self.xs) % 2 == 1:
            line, =self.ax.plot([self.xs[-1], event.xdata], [self.ys[-1], event.ydata], 'r')
            line.figure.canvas.draw()
            self.ax.lines.pop()

class Points():
    def __init__(self):
        self.start_point_x = 0
        self.start_point_y = 0
        self.end_point_x = 0
        self.end_point_y = 0
    def x_start_point(self,point):
        self.start_point_x = numpy.floor(point)

    def y_start_point(self,point):
        self.start_point_y = numpy.floor(point)

    def x_end_point(self,point):
        self.end_point_x = numpy.floor(point)

    def y_end_point(self,point):
        self.end_point_y = numpy.floor(point)

        self.get_all_coordinates()
    def get_all_coordinates(self):
        arr = []
        x_diff = self.end_point_x - self.start_point_x
        y_diff = self.end_point_y - self.start_point_y
        if x_diff == 0 or y_diff == 0:
            m = 0
        else:
            m = (self.end_point_y - self.start_point_y) / (self.end_point_x - self.start_point_x)
        print(m)
        c = self.end_point_y - m * self.end_point_x
        if (self.start_point_x > self.end_point_x):
            for x in range (int(self.start_point_x),int(self.end_point_x+1), -1):
                y = m * x + c
                arr.append([int(numpy.ceil(x)),int(numpy.ceil(y))])


        if(self.end_point_x == self.start_point_x):
            x = self.start_point_x
            if(self.start_point_y > self.end_point_y):
                for y in range(int(numpy.ceil(self.start_point_y)),int(numpy.floor(self.end_point_y)),-1):
                    arr.append([int(numpy.ceil(x)),int(numpy.ceil(y))])
            else:
                for y in range(int(numpy.ceil(self.start_point_y)),int(numpy.floor(self.end_point_y)),1):
                    arr.append([int(numpy.ceil(x)),int(numpy.ceil(y))])
        else:
            for x in range (int(self.start_point_x),int(self.end_point_x+1)):
                y = m * x + c
                arr.append([int(numpy.ceil(x)),int(numpy.ceil(y))])



        print(arr)
        calculate(arr)




def calculate(arr):
    rgb = []
    for x in range(len(arr)):
        x_coordinate = arr[x][0]
        y_coordinate = arr[x][1]
        print(image_tensor.shape)
        red_channel = image_tensor[y_coordinate][x_coordinate][0]
        green_channel = image_tensor[y_coordinate][x_coordinate][1]
        blue_channel = image_tensor[y_coordinate][x_coordinate][2]

        rgb.append([red_channel.numpy(),green_channel.numpy(),blue_channel.numpy()])

    print(rgb)
    calculate_temperature(rgb)

def calculate_temperature(array):
    temp = []
    for x in range(len(array)):

        if array[x][0] > 0.45 and array[x][1] >= 0.45:
            print("hi")
            temp.append((round((13*array[x][0] + 8*array[x][1] + 5.6*array[x][2]),2)))
            continue
        if array[x][0] < 0.1 and array[x][1] >= array[x][2] :
            if(array[x][1] - array[x][2] >= 0.2):
                temp.append((round((15*array[x][0] + 14*array[x][1] + 5*array[x][2]),2)))
            else:
                temp.append((round((15*array[x][0] + 12*array[x][1] + 4*array[x][2]),2)))
            continue
        else:
            print("hello")
            temp.append((round((23*array[x][0] + 10*array[x][1] + 6*array[x][2]),2)))
            continue

    print(temp)
    plot_graph(temp)
def plot_graph(temp_array):
    n = len(temp_array)
    x = np.arange(n)
    fig1, ax1 = plt.subplots()
    ax1.plot(x,temp_array)
    plt.show()

def donecallback(cid1,cid2):
    fig.canvas.mpl_disconnect(cid1)
    fig.canvas.mpl_disconnect(cid2)
    print("hi")
def plot_lines(event):

    global cid1
    global cid2
    cid1 = fig.canvas.mpl_connect('button_press_event', draw_line.mouse_click)
    cid2 = fig.canvas.mpl_connect('motion_notify_event', draw_line.mouse_move)





def main():
    file_path1 = "temp.png"
    file_path1 = Image.open(file_path1)
    file_path1 = ImageOps.flip(file_path1)
    convert_tensor = transforms.ToTensor()

    file_path1 = convert_tensor(file_path1)
    '''
    file_path1 = F.interpolate(file_path1, 160, mode = 'nearest')
    file_path1 = file_path1.swapaxes(2,1)
    file_path1 = F.interpolate(file_path1, 120, mode = 'nearest')
    file_path1 = file_path1.swapaxes(2,1)'''
    file_path1 = file_path1.swapaxes(1,0)
    file_path1 = file_path1.swapaxes(2,1)
    global image_tensor
    image_tensor = file_path1
    global fig
    global ax
    fig, ax = plt.subplots()
    ax.set_ylim([0,500])
    tmp = ax.imshow(file_path1)

    tmp.format_cursor_data = format_cursor_data
    global draw_line
    draw_line = LineBuilder(fig, ax)
    axButn1 = plt.axes([0.91, 0.01, 0.1, 0.1])
    global btn1
    btn1 = Button(axButn1, label="Draw\nLine", color='pink', hovercolor='tomato')
    btn1.on_clicked(plot_lines)
    plt.show()



