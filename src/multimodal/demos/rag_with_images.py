class MultimodalRAG:
    """
    Demo: Retrieving charts and asking GPT-4V.
    """
    
    def query(self, user_question):
        print(f"Retrieving relevant images for '{user_question}'...")
        retrieved_img = "sales_chart.png"
        
        print("Sending image + question to VLM...")
        answer = "Based on the chart, sales grew by 20%."
        return answer
