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
if file is None:
    st.text("Please upload an image file")
    
else:
    f_ex=file.name.split('.')
    if f_ex[1]=='jpeg':
        img=Image.open(file)
        st.image(img.rotate(270),width=300)
        height_percent = (fixed_height / float(img.size[1]))
        width_size = int((float(img.size[0]) * float(height_percent)))
        new_img = img.resize((width_size, fixed_height), Image.ANTIALIAS)
        reader=file_reader()
        with st.spinner("🤖  AI is Working....!"):
            output=reader.readtext(np.array(new_img))
            for item in output:
                x.append(item[1])
            xls = pd.read_excel("./words list - Copy.xlsx",index_col=0).to_dict()
            df=pd.read_excel("./Book2 - Copy.xlsx")


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
        st.image(img1.rotate(270),width=300)
#         st.image(img1,width=300) 
        height_percent1 = (fixed_height / float(img1.size[1]))
        width_size = int((float(img1.size[0]) * float(height_percent1)))
        new_img1 = img1.resize((width_size, fixed_height), Image.ANTIALIAS)
        new_img1=new_img1.rotate(-270)
            # new_img1.save(file)
        reader=file_reader()
        with st.spinner("🤖  AI is Working....!"):
            output=reader.readtext(np.array(new_img1))
            for item in output:
                x.append(item[1])
                
            xls = pd.read_excel("./words list - Copy.xlsx",index_col=0).to_dict()
            df=pd.read_excel("./Book2 - Copy.xlsx")


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
            except:
                st.markdown('Error... Please upload Clear Image 😔 ')
                # st.caption(' Made by Raj..')



