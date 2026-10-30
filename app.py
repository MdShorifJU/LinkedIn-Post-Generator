import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# Load environment variables
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError(
        "GROQ_API_KEY not found. Please add it to your .env file."
    )


# Initialize LLM
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.7,
    api_key=api_key
)


# Tech Writer Agent
tech_writer_prompt = ChatPromptTemplate.from_template("""
You are a professional LinkedIn technology content writer.

Write an engaging LinkedIn post about the given topic.

Requirements:
- Write 2-4 short paragraphs.
- Use a professional and engaging tone.
- Explain the topic clearly.
- Include relevant insights.
- Use suitable emojis where appropriate.
- End with a thoughtful question or call-to-action.
- Write entirely in the requested language.

Topic: {topic}
Language: {language}

Generate only the LinkedIn post.
""")

tech_writer_chain = (
    tech_writer_prompt
    | llm
    | StrOutputParser()
)


# General Writer Agent
general_writer_prompt = ChatPromptTemplate.from_template("""
You are a professional LinkedIn content writer.

Write an engaging LinkedIn post about a general topic such as
education, business, career, leadership, productivity,
or personal development.

Requirements:
- Write 2-4 short paragraphs.
- Use a professional and engaging tone.
- Provide meaningful insights.
- Use suitable emojis where appropriate.
- End with a thoughtful question or call-to-action.
- Write entirely in the requested language.

Topic: {topic}
Language: {language}

Generate only the LinkedIn post.
""")

general_writer_chain = (
    general_writer_prompt
    | llm
    | StrOutputParser()
)


# Router Agent
router_prompt = ChatPromptTemplate.from_template("""
You are a topic classification agent.

Classify the topic into exactly one category.

Tech:
AI, Machine Learning, Programming, Software,
Cybersecurity, Robotics, Data Science, Technology.

General:
Education, Business, Career, Leadership,
Productivity, Lifestyle, Personal Development.

Topic: {topic}

Return ONLY one word:
Tech or General
""")

router_chain = (
    router_prompt
    | llm
    | StrOutputParser()
)


# LinkedIn Post Generator
def linkedin_post_generator(topic, language="English"):

    if not topic or not topic.strip():
        raise ValueError("Topic cannot be empty.")

    if not language or not language.strip():
        raise ValueError("Language cannot be empty.")

    # Step 1: Classify topic
    category = router_chain.invoke({
        "topic": topic
    }).strip()

    print("\nTopic:", topic)
    print("Category:", category)

    # Step 2: Select the appropriate agent
    if category.lower() == "tech":

        print("Selected Agent: Tech Writer Agent")

        result = tech_writer_chain.invoke({
            "topic": topic,
            "language": language
        })

    else:

        print("Selected Agent: General Writer Agent")

        result = general_writer_chain.invoke({
            "topic": topic,
            "language": language
        })

    return result


# Main Program
# if __name__ == "__main__":

#     print("=" * 50)
#     print("AI LINKEDIN POST GENERATOR")
#     print("=" * 50)

#     topic = input("Enter your topic: ").strip()
#     language = input(
#         "Enter language (English/Bengali): "
#     ).strip()

#     try:
#         post = linkedin_post_generator(
#             topic=topic,
#             language=language or "English"
#         )

#         print("\nGenerated LinkedIn Post:")
#         print("=" * 50)
#         print(post)

#     except Exception as error:
#         print("\nError:", error)