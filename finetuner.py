import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

training  = openai.File.create(
                    file=open("primed_data.jsonl", "rb"),
                    purpose='fine-tune'
                    )

openai.FineTuningJob.create(training_file=training, model="gpt-3.5-turbo")

