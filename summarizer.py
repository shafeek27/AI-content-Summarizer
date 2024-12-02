
from transformers import pipeline
pipe = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
summarizer = pipeline("summarization")
def summarize_text(text, max_length=130, min_length=30):
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']
if __name__ == "__main__":
    content = """
    Artificial intelligence (AI) is intelligence demonstrated by machines, in contrast to the natural intelligence 
    displayed by humans and animals. Leading AI textbooks define the field as the study of "intelligent agents": any 
    device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals.
    Colloquially, the term "artificial intelligence" is often used to describe machines (or computers) that mimic "cognitive" 
    functions that humans associate with the human mind, such as "learning" and "problem-solving".
    """
    print("Original Content: \n", content)
    summary = summarize_text(content)
    
    print("\nSummary: \n", summary)
