from fastapi import FastAPI
from pydantic import BaseModel
import os
from fastapi.responses import JSONResponse
from agent.agentic_workflow import GraphBuilder
app=FastAPI()

class QueryRequest(BaseModel):
    question:str

@app.post('/query')
async def query_travel_agent(query:QueryRequest):
    try:
        print(f'query from user={query}')
        graph=GraphBuilder(model_provider='groq')
        react_app=graph()

        png_graph=react_app.get_graph().draw_mermaid_png()
        
        with open('my_graph.png','wb') as file:
            file.write(png_graph)

        print(f'graph saved as my_graph.png at {os.getcwd()}')

        messages={'messages':[query.question]}

        output=react_app.invoke(messages)

        if isinstance(output,dict) and "messages" in output:
            final_output=output['messages'][-1].content
        else:
            final_output=str(output)

        return JSONResponse(content=final_output,status_code=200)

    
    except Exception as e:
        return JSONResponse(content={'error':str(e)},status_code=500)



