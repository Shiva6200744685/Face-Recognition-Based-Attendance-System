from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class train:
     def __init__(self,root):
          self.root=root
          self.root.geometry("1530x790+0+0")
          self.root.title("Face Recognition System")

          title_lbl=Label(self.root,text="TRAIN DATA SET",font =("times new roman",35,"bold"),bg="white",fg="red")
          title_lbl.place(x=0,y=0,width=1530,height=45)

          img_top=Image.open("C:/Users/happy/Desktop/Face recognition system/college_images/facialrecognition.png")
          img_top=img_top.resize((1530,325),Image.BILINEAR)
          self.photoimg_top=ImageTk.PhotoImage(img_top)

          f_lbl=Label(self.root,image=self.photoimg_top)
          f_lbl.place(x=0,y=55,width=1530,height=325)

        #   button
          b1=Button(self.root,text="TRAIN DATA",cursor="hand2",font =("times new roman",30,"bold"),bg="red",fg="white")
          b1.place(x=0,y=380,width=1530,height=60)


          img_bottom=Image.open("C:/Users/happy/Desktop/Face recognition system/college_images/opencv_face_reco_more_data.jpg")
          img_bottom=img_bottom.resize((1530,325),Image.BILINEAR)
          self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

          f_lbl=Label(self.root,image=self.photoimg_bottom)
          f_lbl.place(x=0,y=440,width=1530,height=325)



  





          
if __name__ == "__main__":
     root=Tk()
     obj=train(root)
     root.mainloop()