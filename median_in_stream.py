#NOT SOLVED : should imitate avl tree


#median
# if len is even median=(array[N/2 -1]+ array[N/2])/2
# if len is odd median=array[N//2] round down


# if len(array)==1:
#     median =array[0]
# if len(array)=2
#     median =(array[0]+array[1])/2

# buffer1=[] # N/2-1 and N/2
# buffer2=[] # N//2

# stream=[1]
# median=1 buffer2=[1]
# stream =[1,5] 
# median =3 buffer2[ 1,5]

# stream[1,5,8]
# if new_element > buffer2[1]: median=buffer2[1] -->update buffer1 with median
# stream[1,5,0]
# elif new_element< buffer2[0]: median=buffer2[0] -->update buffer1 with median
# stream=[1,5,3]
# else median =new element  -->update buffer2 with median

# stream[1,5,3,4]
# if new element > buffer1[0] :median =(buffer1[0]+new_element)/2 -->update buffer2 with median and buffer1[0]
# stream[1,5,3,2]

# if new element < buffer1[0] :median =(new_element buffer1[0]+)/2 -->update buffer2 with buffer1[0] and median 

import random

def find_median_of_stream():
    stream=[]
    buffer=[0,0]
    median=0
    i=0
    while i<10:
        new_element=random.randint(0,50)
        stream.append(new_element)
        print('stream: ',stream)

        if len(stream)==1:
            median=stream[0]
        elif len(stream)==2:
            median =(stream[0]+stream[1])//2
            buffer[0]=min(stream)
            buffer[1]=max(stream)
        else:
            if len(stream)%2==1 :
                if new_element > buffer[1]: 
                    median=buffer[1]
                elif new_element< buffer[0]: 
                    median=buffer[1]
                    buffer[1]=buffer[0]
                    buffer[0]=new_element
                else: 
                    median =new_element 
                    buffer[1]=new_element
                             
            elif len(stream)%2==0 :
                if new_element <buffer[1] and new_element > buffer[0]:
                    #buffer[0]=new_element
                    buffer[1]= new_element
                    median =(buffer[0]+buffer[1])//2 

                else :
                    median =(buffer[0]+buffer[1])//2 
                    

        i+=1
        print(buffer)
        print(median)


find_median_of_stream()



        


