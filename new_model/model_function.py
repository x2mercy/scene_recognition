#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 21:04:14 2017

@author: chenrui
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import json
import argparse
import sys
import tensorflow as tf
buildingset=["pho compressed", "arthur compressed", "audi compressed", "aa compressed", "chapel compressed",\
             "nutrition building-compressed", "classical studies department-compressed",  "college of general study-compressed",\
             "Gym-compressed","college of fine arts-compressed", "Questrom School of Business-compressed","Tsai Performance Center-compressed",\
             "college of communication-compressed"]
def dataTojson(buildingname):
    data = {}
    if buildingname == "pho compressed":
        data['name']= "Photonics Center"
        data['categories'] = "Engineering"
        data['address'] = "8 St Marys St, Boston, MA 02215"
        data['image_url'] = "https://i.pinimg.com/originals/b6/9d/93/b69d93ed4d468789bec1ddc6728226d4.jpg"
        data['lat'] = 42.3494683
        data['lng'] = 0-71.1064357
        data['url'] = "https://personal-homepage-for-yize-liu.firebaseapp.com/pho.html"
        
        
    if buildingname == "arthur compressed":
        data['name']= "Arthur G.B. Metcalfe Center for Science & Engineering"
        data['categories'] = "Science and Engineering"
        data['address'] = "590 Commonwealth Avenue, Boston, MA 02215"
        data['image_url'] = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Metcalf_Center_for_Science_and_Engineering.JPG/1200px-Metcalf_Center_for_Science_and_Engineering.JPG"
        data['lat'] = 42.342415297
        data['lng'] = -71.1001079329
        data['url'] = "https://personal-homepage-for-yize-liu.firebaseapp.com/AMC.html"
        
    if buildingname == "audi compressed":
        data['name']= "Alfred L. Morse Auditorium"
        data['categories'] = "public"
        data['address'] = "602 Commonwealth Avenue, Boston, MA 02215"
        data['image_url'] = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Morsefront.JPG/300px-Morsefront.JPG"
        data['lat'] = 42.3490759
        data['lng'] = -71.1030856
        data['url'] = "https://personal-homepage-for-yize-liu.firebaseapp.com/Audit.html"
        
    if buildingname == "aa compressed":
        data['name']= "Agganis Arena"
        data['categories'] = "multi-purpose arena"
        data['address'] = "925 Commonwealth Avenue, Boston, MA 02215"
        data['image_url'] = "https://www.cannondesign.com/assets/BostonU-RecCtr_1.jpg"
        data['lat'] = 42.356482
        data['lng'] = -71.117903
        data['url'] = "https://personal-homepage-for-yize-liu.firebaseapp.com/index_aa.html"
        
    if buildingname == "chapel compressed":
        data['name']= "Marsh Chapel"
        data['categories'] = "official place of worship"
        data['address'] = "735 Commonwealth Avenue, Boston, MA 02215"
        data['image_url'] = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Boston_University_Marsh_Chapel%2C_Boston_MA.jpg/1200px-Boston_University_Marsh_Chapel%2C_Boston_MA.jpg"
        data['lat'] = 42.3505958
        data['lng'] = -71.1086339
        data['url'] = "https://personal-homepage-for-yize-liu.firebaseapp.com/page3_chapel/index_chapel.html"

    if buildingname == "nutrition building-compressed":
        data['name']= "Boston Univeristy Nutrition"
        data['categories'] = "Nutrition Center"
        data['address'] = "881 Commonwealth Avenue, Boston, MA 02215"
        data['image_url'] = "https://media.thetab.com/blogs.dir/92/files/2015/11/IMG_7455-e1447884989651-768x1024.jpg"
        data['lat'] = 42.3518076
        data['lng'] = -71.117406
        data['url'] = "http://www.bu.edu/scnc/"
        
    if buildingname == "classical studies department-compressed":
        data['name']= "Department of Classical Studies"
        data['categories'] = "Classics"
        data['address'] = "745 Commonwealth Avenue, Boston, MA 02215"
        data['image_url'] = "https://images.noodle.com/profiles/college_institution/coG/photos/110405_BostonU_Wiki.jpg"
        data['lat'] = 42.3503658
        data['lng'] = -71.1069438
        data['url'] = "http://www.bu.edu/classics/"
        
    if buildingname == "college of general study-compressed":
        data['name']= "College of General Studies"
        data['categories'] = "General Studies"
        data['address'] = "871 Commonwealth Avenue, Boston, MA 02215"
        data['image_url'] = "http://dailyfreepress.com/wp-content/uploads/2014/06/DSCF2856.jpg"
        data['lat'] = 42.351496
        data['lng'] = 0-71.114568
        data['url'] = "http://www.bu.edu/cgs/"
        
    if buildingname == "Gym-compressed":
        data['name']= "Boston University Fitness and Recreation Center"
        data['categories'] = "gym"
        data['address'] = "915 Commonwealth Avenue, Boston, MA 02215"
        data['image_url'] = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/BU_Fitrec.jpg/1200px-BU_Fitrec.jpg"
        data['lat'] = 42.3518687
        data['lng'] = -71.1186489
        data['url'] = "https://www.bu.edu/fitrec/"

    if buildingname == "college of fine arts-compressed":
        data['name']= "college of fine arts"
        data['categories'] = "CAS"
        data['address'] = "855 Commonwealth Avenue, Boston, MA 02215"
        data['image_url'] = "http://eroonkang.com/content/2.about/390.boston-university/bostonuniv.jpg"
        data['lat'] = 42.3514989
        data['lng'] = -71.1157154
        data['url'] = "https://www.bu.edu/cfa/"

    if buildingname == "Questrom School of Business-compressed":
        data['name']= "Questrom school of business"
        data['categories'] = "Buisness School"
        data['address'] = "595 Commonwealth Avenue, Boston, MA 02215"
        data['image_url'] = "https://poetsandquants.com/wp-content/uploads/2016/04/Boston_business-500x250.jpg"
        data['lat'] = 42.349626
        data['lng'] = -71.1017353
        data['url'] = "http://www.bu.edu/questrom/"
        
    if buildingname == "Tsai Performance Center-compressed":
        data['name']= "Tsai Performance Center"
        data['categories'] = "Concert"
        data['address'] = "685 Commonwealth Avenue, Boston, MA 02215"
        data['image_url'] = "https://c1.staticflickr.com/1/55/150801039_f84756fd5d_b.jpg"
        data['lat'] = 42.3501152
        data['lng'] = -71.1067635
        data['url'] = "http://www.bu.edu/tsai/"
        
    if buildingname == "college of communication-compressed":
        data['name']= "College of Communication"
        data['categories'] = "COM"
        data['address'] = "640 Commonwealth Avenue, Boston, MA 02215"
        data['image_url'] = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/BU_College_of_Communication.jpg/300px-BU_College_of_Communication.jpg"
        data['lat'] = 42.3493904
        data['lng'] = -71.1023502
        data['url'] = "http://www.bu.edu/com/"




#    fl=open('bubuilding.js', 'w')
#    #fl=open('../out/map_polyline.js', 'a')
#    #fl.write(json.dumps(datas))
#    fl.write(json.dumps(data,ensure_ascii=False,indent=2))
#    fl.close()
    return data 
 
def run_graph(image_data, labels, input_layer_name, output_layer_name,
              num_top_predictions):
  with tf.Session() as sess:
    # Feed the image_data as input to the graph.
    #   predictions will contain a two-dimensional array, where one
    #   dimension represents the input image count, and the other has
    #   predictions per class
    softmax_tensor = sess.graph.get_tensor_by_name(output_layer_name)
    predictions, = sess.run(softmax_tensor, {input_layer_name: image_data})

    # Sort to show labels in order of confidence
    top_k = predictions.argsort()[-num_top_predictions:][::-1]
    num = 0
    for node_id in top_k:
      human_string = labels[node_id]
#      score = predictions[node_id]
#      print('%s (score = %.5f)' % (human_string, score))
      if num == 0:
          result=[]
          result.append(dataTojson(human_string))
          seconditem=""
          for temp in buildingset:
              if temp != human_string:
                  result.append(dataTojson(temp))
                  seconditem=temp
                  break
          for temp in buildingset:
              if temp != human_string and temp != seconditem:
                  result.append(dataTojson(temp))
                  break
          return json.dumps(result)
#          num=num+1
          
def load_image(filename):
  """Read in the image_data to be classified."""
  return tf.gfile.FastGFile(filename, 'rb').read()


def load_labels(filename):
  """Read in labels, one label per line."""
  return [line.rstrip() for line in tf.gfile.GFile(filename)]


def load_graph(filename):
  """Unpersists graph from file as default graph."""
  with tf.gfile.FastGFile(filename, 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    tf.import_graph_def(graph_def, name='') 
    
def model(image_path):
    image_data = load_image(image_path)
    labels = load_labels('output_labels.txt')
    load_graph('output_graph.pb')
    return run_graph(image_data, labels, 'DecodeJpeg/contents:0', 'final_result:0',
            5)
    
#print(model("temp.jpg"))
#def main():
#  """Runs inference on an image."""
#  print(model('/Users/chenrui/Desktop/code/test/pho.jpg'))
#
#if __name__ == '__main__':
#  main()   


