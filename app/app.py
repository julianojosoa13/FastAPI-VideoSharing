from fastapi import FastAPI, HTTPException
from app.schema import PostCreate, PostResponse

app = FastAPI()

text_posts = {
    1: {
        "title": "Basic Arithmetic",
        "content": "What is the result of \(3 + 4\)?"
    },
    
    2: {
        "title": "Coding Challenges",
        "content": "Write a simple Python program to print 'Hello World'."""
    },
    
    3: {
        "title": "Grammar Rules",
        "content": "What is the correct spelling of 'mother-in-law'? (Simpler version: No hyphens, but keep them in words.)"
    },
    
    4: {
        "title": "Creative Writing Tips",
        "content": "How can you make a character in your story have a different personality? (Can include some dialogue and setting details.)"
    },
    
    5: {
        "title": "Understanding Concepts",
        "content": "What is the difference between \(a^2 + b^2\) and \((a + b)^2\)?"
    },
    
    6: {
        "title": "Writing Assignments",
        "content": "Explain how to use an Excel formula that will calculate compound interest. (Include a brief example.)"
    },
    
    7: {
        "title": "Understanding English",
        "content": "Can you explain what the word 'overly' means in the sentence: 'This is very overly long.'?"
    },
    
    8: {
        "title": "Understanding Spanish",
        "content": "How do you say 'goodbye' to someone on social media? (Use a real-life example.)"
    },
    
    9: {
        "title": "Understanding Business",
        "content": "What is the primary difference between a revenue and a profit? Can you give examples of each?"
    },
    
    10: {
        "title": "Understanding History",
        "content": "Who were the main contributors to the American Civil War? (Can include key events in the war.)"
    }
}

@app.get("/posts")
def get_all_posts(limit: int = None):
    posts_list = list(text_posts.values())
    if limit:
        return posts_list[:limit]
    return posts_list

@app.get("/posts/{id}")
def get_post_by_id(id : int):
    if id not in text_posts:
        raise HTTPException(404, "Post Not Found")
    else:
        return text_posts.get(id)

@app.post("/posts")
def create_post(post: PostCreate) ->  PostResponse: 
    new_post = {"title": post.title, "content": post.content}
    text_posts[max(text_posts.keys()) + 1] = new_post 
    return new_post
