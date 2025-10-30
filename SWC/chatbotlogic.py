import google.generativeai as genai

conversation_history = []

def get_response(user_input, scraped_data):
    
    genai.configure(api_key="AIzaSyAn726Chm0tAhjqxfNEg3R125bvbPk_Iu8")
    model = genai.GenerativeModel("gemini-1.5-flash")  

  
    system_message = "You are a helpful assistant."

    
    if scraped_data:
        context = f"Here is some information you can use to assist the user and do not answer in detail:\n{scraped_data}\n"
    else:
        context = ""

    conversation_history.append(f"User: {user_input}")

   
    full_conversation = f"{system_message}\n{context}\n" + "\n".join(conversation_history) + "\nAssistant:"


    response = model.generate_content(full_conversation)

 
    conversation_history.append(f"Assistant: {response.text}")

    return response.text
