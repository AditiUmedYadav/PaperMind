import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

def get_user_collection(user_id: str, doc_id: str):
    # pm_ prefix = PaperMind namespace
    collection_name = f"pm_user_{user_id[:8]}_doc_{doc_id[:8]}"
    return client.get_or_create_collection(collection_name)

def delete_user_collection(user_id: str, doc_id: str):
    collection_name = f"pm_user_{user_id[:8]}_doc_{doc_id[:8]}"
    try:
        client.delete_collection(collection_name)
    except Exception:
        pass  # already deleted or never created

def list_user_collections(user_id: str):
    prefix = f"pm_user_{user_id[:8]}"
    all_cols = client.list_collections()
    return [c for c in all_cols if c.name.startswith(prefix)]