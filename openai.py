# from openai import OpenAi

# client =OpenAi(api_key=)

# responce= client.responses.create(
#     model="gpt-5.4",
#     input="write a short bedtime story about a unicom"
# )


# # imput=[
# #     {
# #         "role":"user","content":"3+4","find a"
# #     },
# #     {
# #         "role":"system","content":"act like a maths teacher"
# #     }

# # ]

# # print(response.output_text)

# # input=[{
# #     "role":"user","content":[
# #         {
# #             "type ":"input_text",
# #             "text":"which contry flag in the omage"
# #         }
# #         {
# #             "type":"input_image",
# #             "image_url":"image link paste here"
# #         }
# #     ]
# # }]




# # quers ansere
# # email summarize

# # class personalAssistant:
# #     def __init__(self):
# #         print("hi i am a king man in the world and we are a greate man")

#     # def and_query (questions):
#     #     responce=client.responce.create(
#     #         model="gpt-5.4"
#     #         input="a+2=7,find a"
#     #     )

#     #     print(responce.output_text)



# class personalAssitant:
#     def __init__(self):
#      print("hi i am your ai assistant how i can help you")
#     def and_query(self):
#     quastion=input("ask me anything")
#     responce=client.responce.create(
#        model="gpt-5.4",
#        input=[
#           {
#              "role":"system","content":"act like a helpful personal assistant"
#           },
#           {
#             "role":"user","content":question
#           }
#        ],
#        tempeature=0.7
#        max_ouput_tokens=512
#     )

#     print(responce.ouput_text.strip())



import base64

# image bassed 64 encode string decode


responce = client.responce.create(
    model="gpt-5",
    input="generate an image of a highly detailed futurestic flaying a nubula",
    tools=[{"type":"image_generation"}]
)

image_data=[
    ouput.result
    for ouput in responce.output
    if output.type== "image_generation_call"

]

if image_base:
image_base64=image_Data[0]
with open ("spaceship.png","wp") as f:
    image_byte=base64.b64decode(image_base64)
    f.write(image_byte)













    # image generation api
prompt="generate an image a highly detaild spacship near a nebula"
result=client.image.generate(
    model="gpt-image-1.5",
    prompt=prompt

)


iamge_base64=result.data[0].64_json
image_bytes = base64.b64decode(image_base64)

with open ("spaceship_image.png","wp") as f:
    f.write(image_byptes)












# edit



prompt=" take the reference image and convert the spaceship color to red"

result=client.image.edit(
    model="gpt-image-1.5",
    prompt=prompt
oepn ("spaceship_image.png","rb")
)


iamge_base64=result.data[0].64_json
image_bytes = base64.b64decode(image_base64)

with open ("red_spaceship_image.png","wp") as f:
    f.write(image_byptes)

