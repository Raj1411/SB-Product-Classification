import easyocr
from IPython.display import Image
from easyocr.easyocr import Reader
import pandas as pd
import os,glob
import streamlit as st
import xlrd
from PIL import Image, ImageOps, ExifTags
from time import  sleep
import streamlit as st
import numpy as np
import re
import io, base64


# ''' This code is for training Images  '''

# reader = easyocr.Reader(['en'],gpu=False)
path_1="D:\Projects\Swiss Beauty Image Classification\More Test Images Text from Image"
save_path='D:\\Projects\\Swiss Beauty Image Classification\\More Test Images Text from Image\\resized'

x=[]


# for file in os.listdir(path_1):
#     img=Image.open(path_1+"\\"+file)
#     fn,fe=os.path.splitext(file)
#     img.thumbnail((600,600),Image.ANTIALIAS)
#     img.save(save_path+"\\"+fn+fe)
#     rotations=[0,-90,180,90]
#     qq=1
#     fixed_height=500
#     for rotation in rotations:
#         height_percent = (fixed_height / float(img.size[1]))
#         width_size = int((float(img.size[0]) * float(height_percent)))
#         img = img.resize((width_size, fixed_height), Image.NEAREST)
#         nn=img.rotate(rotation)
#         nn.save(save_path+"\\"+fn+"-"+str(qq)+fe)
#         qq+=1
            

# for q in os.listdir(save_path):
#     output = reader.readtext(os.path.join(save_path, q))
#     for item in output:
#         x.append(item[1])

# df=pd.DataFrame([x]).transpose()
# df.to_excel(os.path.join(save_path,"words list-1.xlsx"))





# '''  This Code is Final   '''


# rotaions=[0,-90,180,90]
# fixed_height=500
# x=[]
# path_2=input('Enter Image path:  ')
# for rotaion in rotaions:
#     reader=easyocr.Reader(['en'])
#     img=Image.open(path_2)
#     fn,fe=os.path.splitext(path_2)
#     height_percent = (fixed_height / float(img.size[1]))
#     width_size = int((float(img.size[0]) * float(height_percent)))
#     new_img = img.resize((width_size, fixed_height), Image.NEAREST)
#     new_img1=new_img.rotate(rotaion)
#     new_img1.save(path_2)
#     sleep(0)
#     output=reader.readtext(path_2)
#     for item in output:
#         x.append(item[1])





# xls = pd.read_excel("D:\Projects\Swiss Beauty Image Classification\words list - Copy.xlsx",index_col=0).to_dict()

# for i in xls:
#     xls=xls[i]

# xx=[]
# xxx=[]
# for ii in xls:
#     for jj in x:
#         if ii==jj:
#             xx.append(ii+":"+xls.get(jj))
#             for aq in xx:
#                 az=aq.split(":")
#                 for t in az:
#                     if az[1]==xls.get(jj):
#                         xxx.append(az[1])

# print(x)        
# print(xx)
# print('This Product is:  '+xxx[0])























# '''  Code to Streamlit  '''
@st.cache(allow_output_mutation=True)
def file_reader():
    reader=easyocr.Reader(['en'])
    return reader

st.write("""# Swiss Beauty Product Classification """ )

file = st.sidebar.file_uploader("Please upload an file", type=["jpg", "png","jpeg"])
st.set_option('deprecation.showfileUploaderEncoding', False)

fixed_height=500
x=[]
# path_2=input('Enter Image path:  ')
if file is None:
    st.text("Please upload an image file")
    
else:
    # for rotaion in rotaions:
    f_ex=file.name.split('.')
    # print(f_ex[1])
    if f_ex[1]=='jpeg':
        img=Image.open(file)
        st.image(img,width=300)
        height_percent = (fixed_height / float(img.size[1]))
        width_size = int((float(img.size[0]) * float(height_percent)))
        new_img = img.resize((width_size, fixed_height), Image.ANTIALIAS)
        reader=file_reader()
        with st.spinner("🤖  AI is Working....!"):
            output=reader.readtext(np.array(new_img))
            for item in output:
                x.append(item[1])
            # print(x)
            xls = pd.read_excel("D:\Projects\Swiss Beauty Image Classification\words list - Copy.xlsx",index_col=0).to_dict()
            df=pd.read_excel("D:\Projects\Swiss Beauty Image Classification\Book2 - Copy.xlsx")


            xx=[]
            xxx=[]
            for i in xls:
                xls=xls[i]
                for ii in xls:
                    for jj in x:
                        if ii==jj:
                            xx.append(ii+":"+xls.get(jj))
                            for aq in xx:
                                az=aq.split(":")
                                for t in az:
                                    if az[1]==xls.get(jj):
                                        xxx.append(az[1])
            
            
            try:
                result='This Product is:  '+xxx[0]+"     "+'😎'
                font_color= f'<p style="font-family: American Typewriter ; background-color:red; color:white; font-size: 42px;">{result}</p>'
                st.markdown(font_color, unsafe_allow_html=True)
                df1=pd.DataFrame([df[df['sku code']==str(xxx[0])].iloc[0]['Product Name'],
                df[df['sku code']==str(xxx[0])].iloc[0]['Color/Group'],
                df[df['sku code']==str(xxx[0])].iloc[0]['Rating'],
                df[df['sku code']==str(xxx[0])].iloc[0]['MRP'],
                df[df['sku code']==str(xxx[0])].iloc[0]['Net.wet'],
                df[df['sku code']==str(xxx[0])].iloc[0]['Actual Description on products'],
                df[df['sku code']==str(xxx[0])].iloc[0]['Status of pics'],
                df[df['sku code']==str(xxx[0])].iloc[0]['Checked by Renuka'],
                df[df['sku code']==str(xxx[0])].iloc[0]['Product Dimensions'].replace('\n',', '),
                df[df['sku code']==str(xxx[0])].iloc[0]['Buy LInk'],
                df[df['sku code']==str(xxx[0])].iloc[0]['HSN'].astype(int),
                df[df['sku code']==str(xxx[0])].iloc[0]['How to use'],
                df[df['sku code']==str(xxx[0])].iloc[0]['Key Benefit'],
                df[df['sku code']==str(xxx[0])].iloc[0]['Difference from other'],
                df[df['sku code']==str(xxx[0])].iloc[0]['Hero Ingredients'],
                df[df['sku code']==str(xxx[0])].iloc[0]['Category'],
                df[df['sku code']==str(xxx[0])].iloc[0]['ARTIST TIP'],
                df[df['sku code']==str(xxx[0])].iloc[0]['Before / After'],
                df[df['sku code']==str(xxx[0])].iloc[0]['ARTIST TIP'],
                df[df['sku code']==str(xxx[0])].iloc[0]['Name of Wev']],columns=['Product Details'],index=[
                'Product Name','Color/Group','Rating','MRP','Net.wet','Actual Description on products','Status of pics','Checked by Renuka',
                'Product Dimensions','Buy LInk','HSN','How to use','Key Benefit','Difference from other','Hero Ingredients','Category',
                'ARTIST TIP','Before / After','ARTIST TIP-1','Name of Wev'])
                html = """\
                        <html>  
                        <head></head>
                        <table border="0" 
                        align="center">
                        <body> {0}
                            <br> </br>
                            <br> </br>
                            <br> </br>
                            <br> </br>
                            </table>
                        </body>
                        </html>
                """.format(df1.to_html(index=True,header=False))
                st.markdown(html,unsafe_allow_html=True)
                # st.caption(' Made by Raj..')
                # st.markdown(f'<p style="font-family: American Typewriter ; background-color:red; color:white; font-size: 20px;">{caption}</p>',unsafe_allow_html=True)
            except:
                st.markdown('Error... Please upload Clear Image 😔 ')
                # st.caption(' Made by Raj..')
                
    else:
        img1=Image.open(file)
        st.image(img1.rotate(-90),width=300)
        height_percent1 = (fixed_height / float(img1.size[1]))
        width_size = int((float(img1.size[0]) * float(height_percent1)))
        new_img1 = img1.resize((width_size, fixed_height), Image.ANTIALIAS)
        new_img1=new_img1.rotate(-90)
            # new_img1.save(file)
        reader=file_reader()
        with st.spinner("🤖  AI is Working....!"):
            output=reader.readtext(np.array(new_img1))
            for item in output:
                x.append(item[1])
                # print(x)
                
            xls = pd.read_excel("D:\Projects\Swiss Beauty Image Classification\words list - Copy.xlsx",index_col=0).to_dict()
            df=pd.read_excel("D:\Projects\Swiss Beauty Image Classification\Book2 - Copy.xlsx")


            xx=[]
            xxx=[]
            for i in xls:
                xls=xls[i]
                for ii in xls:
                    for jj in x:
                        if ii==jj:
                            xx.append(ii+":"+xls.get(jj))
                            for aq in xx:
                                az=aq.split(":")
                                for t in az:
                                    if az[1]==xls.get(jj):
                                        xxx.append(az[1])
                # print(xxx)
            try:
                result='This Product is:  '+xxx[0]+"     "+'😎'
                font_color= f'<p style="font-family: American Typewriter ; background-color:red; color:white; font-size: 42px;">{result}</p>'
                st.markdown(font_color, unsafe_allow_html=True)
                df1=pd.DataFrame([df[df['sku code']==str(xxx[0])].iloc[0]['Product Name'],
                df[df['sku code']==str(xxx[0])].iloc[0]['Color/Group'],
                df[df['sku code']==str(xxx[0])].iloc[0]['Rating'],
                df[df['sku code']==str(xxx[0])].iloc[0]['MRP'],
                df[df['sku code']==str(xxx[0])].iloc[0]['Net.wet'],
                df[df['sku code']==str(xxx[0])].iloc[0]['Actual Description on products'],
                df[df['sku code']==str(xxx[0])].iloc[0]['Status of pics'],
                df[df['sku code']==str(xxx[0])].iloc[0]['Checked by Renuka'],
                df[df['sku code']==str(xxx[0])].iloc[0]['Product Dimensions'].replace('\n',', '),
                df[df['sku code']==str(xxx[0])].iloc[0]['Buy LInk'],
                df[df['sku code']==str(xxx[0])].iloc[0]['HSN'].astype(int),
                df[df['sku code']==str(xxx[0])].iloc[0]['How to use'],
                df[df['sku code']==str(xxx[0])].iloc[0]['Key Benefit'],
                df[df['sku code']==str(xxx[0])].iloc[0]['Difference from other'],
                df[df['sku code']==str(xxx[0])].iloc[0]['Hero Ingredients'],
                df[df['sku code']==str(xxx[0])].iloc[0]['Category'],
                df[df['sku code']==str(xxx[0])].iloc[0]['ARTIST TIP'],
                df[df['sku code']==str(xxx[0])].iloc[0]['Before / After'],
                df[df['sku code']==str(xxx[0])].iloc[0]['ARTIST TIP'],
                df[df['sku code']==str(xxx[0])].iloc[0]['Name of Wev']],columns=['Product Details'],index=[
                'Product Name','Color/Group','Rating','MRP','Net.wet','Actual Description on products','Status of pics','Checked by Renuka',
                'Product Dimensions','Buy LInk','HSN','How to use','Key Benefit','Difference from other','Hero Ingredients','Category',
                'ARTIST TIP','Before / After','ARTIST TIP-1','Name of Wev'])
                html = """\
                    <html>  
                    <head></head>
                    <table border="0" 
                    align="center">
                    <body> {0}
                        <br> </br>
                        <br> </br>
                        <br> </br>
                        <br> </br>
                    </table>
                    </body>
                    </html>
                """.format(df1.to_html(index=True,header=False))
                st.markdown(html,unsafe_allow_html=True)
                # st.caption(' Made by Raj..')
            except:
                st.markdown('Error... Please upload Clear Image 😔 ')
                # st.caption(' Made by Raj..')



