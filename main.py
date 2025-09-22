import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew 
from langchain_groq import ChatGroq

load_dotenv()  # Load environment variables from .env file
groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    api_key=groq_api_key,
    model="groq/llama-3.3-70b-versatile"  # Updated to supported production model
)

# Define agents
planner = Agent(
    role="Content Planner",
    goal="Plan engaging and factually accurate content on {topic}",
    backstory="You are responsible for creating a detailed outline...",
    allow_delegation=False,
    verbose=True,
    llm=llm
)

writer = Agent(
    role="Content Writer",
    goal="Write insightful and factually accurate opinion pieces about {topic}",
    backstory="You expand the planner’s outline into a full draft...",
    allow_delegation=False,
    verbose=True,
    llm=llm
)

editor = Agent(
    role="Editor",
    goal="Edit a given blog post to align with journalistic style.",
    backstory="You polish the content so it fits the brand voice...",
    allow_delegation=False,
    verbose=True,
    llm=llm
)

# Define tasks
plan = Task(
    description="Research trends, audience, SEO, and make a blog outline on {topic}.",
    expected_output="A structured outline with intro, body, conclusion, keywords, and references.",
    agent=planner
)

write = Task(
    description="Expand the planner’s outline into a full blog article.",
    expected_output="A complete blog article in markdown format.",
    agent=writer
)

edit = Task(
    description="Polish the blog article to make it ready for publishing.",
    expected_output="Final version of the blog post, error-free and styled.",
    agent=editor
)

# Create crew
crew = Crew(
    agents=[planner, writer, editor],
    tasks=[plan, write, edit],
    verbose=True
)

if __name__ == "__main__":
    topic = "Artificial Intelligence in Education"
    result = crew.kickoff(inputs={"topic": topic})
    print(result)