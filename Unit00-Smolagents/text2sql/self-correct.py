
# https://huggingface.co/docs/smolagents/examples/text_to_sql

!pip install smolagents python-dotenv sqlalchemy --upgrade -q


from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    String,
    Integer,
    Float,
    insert,
    inspect,
    text,
)

engine = create_engine("sqlite:///:memory:")
metadata_obj = MetaData()

def insert_rows_into_table(rows, table, engine=engine):
    for row in rows:
        stmt = insert(table).values(**row)
        with engine.begin() as connection:
            connection.execute(stmt)

table_name = "receipts"
receipts = Table(
    table_name,
    metadata_obj,
    Column("receipt_id", Integer, primary_key=True),
    Column("customer_name", String(16), primary_key=True),
    Column("price", Float),
    Column("tip", Float),
)
metadata_obj.create_all(engine)

rows = [
    {"receipt_id": 1, "customer_name": "Alan Payne", "price": 12.06, "tip": 1.20},
    {"receipt_id": 2, "customer_name": "Alex Mason", "price": 23.86, "tip": 0.24},
    {"receipt_id": 3, "customer_name": "Woodrow Wilson", "price": 53.43, "tip": 5.43},
    {"receipt_id": 4, "customer_name": "Margaret James", "price": 21.11, "tip": 1.00},
]
insert_rows_into_table(rows, receipts)

inspector = inspect(engine)
columns_info = [(col["name"], col["type"]) for col in inspector.get_columns("receipts")]

table_description = "Columns:\n" + "\n".join([f"  - {name}: {col_type}" for name, col_type in columns_info])
print(table_description)

# Create the tool
from smolagents import tool

@tool
def sql_engine(query: str) -> str:
    """
    Allows you to perform SQL queries on the table. Returns a string representation of the result.
    The table is named 'receipts'. Its description is as follows:
        Columns:
        - receipt_id: INTEGER
        - customer_name: VARCHAR(16)
        - price: FLOAT
        - tip: FLOAT

    Args:
        query: The query to perform. This should be correct SQL.
    """
    output = ""
    with engine.connect() as con:
        rows = con.execute(text(query))
        for row in rows:
            output += "\n" + str(row)
    return output

# Create the agent
from smolagents import CodeAgent, LiteLLMModel

# Optiplex9020-1/WIN10
# 2025MAY03
# Trying with gemma3:4b [Process ok, perfect answer]
# Max RAM: ? / 126 sec = 2.1 min
model = LiteLLMModel(
    model_id="ollama_chat/gemma3:4b",
    api_base="http://localhost:11434",
)
agent = CodeAgent(
    model = model,
    tools = [sql_engine]
)
agent.run("Can you give me the name of the client who got the most expensive receipt?")
╭──────────────────────────────────────────── New run ─────────────────────────────────────────────╮
│                                                                                                  │
│ Can you give me the name of the client who got the most expensive receipt?                       │
│                                                                                                  │
╰─ LiteLLMModel - ollama_chat/gemma3:4b ───────────────────────────────────────────────────────────╯
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Step 1 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ─ Executing parsed code: ─────────────────────────────────────────────────────────────────────────
  result = sql_engine(query="SELECT customer_name FROM receipts ORDER BY price DESC LIMIT 1")
  print(result)
  final_answer(result)
 ──────────────────────────────────────────────────────────────────────────────────────────────────
Execution logs:

('Woodrow Wilson',)

Out - Final answer:
('Woodrow Wilson',)
[Step 1: Duration 126.20 seconds| Input tokens: 2,296 | Output tokens: 80]
Out[5]: "\n('Woodrow Wilson',)"

agent.run("How much did thid client tip?")