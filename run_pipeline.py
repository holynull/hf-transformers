from transformers import pipeline

if __name__=="__main__":
    while True:
        generatoro=pipeline(model="gpt2",task="text-generation")
        user_input=input()
        result=generatoro([user_input],max_length=1024)
        print(result[0][0]["generated_text"])