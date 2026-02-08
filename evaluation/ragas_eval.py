from ragas import evaluate
from ragas.metrics.collections import (
    faithfulness,
    answer_relevancy,
    context_precision,
    context_recall,
)
from datasets import Dataset

from app.rag.pipeline import run_rag
from evaluation.ragas_embeddings import get_ragas_embeddings
from evaluation.eval_dataset import load_eval_dataset


def run_evaluation():
    raw_data = load_eval_dataset()

    rows = []
    for item in raw_data:
        answer, contexts = run_rag(item["question"], return_contexts=True)

        rows.append({
            "question": item["question"],
            "answer": answer,
            "contexts": contexts,
            "ground_truth": item["ground_truth"],
        })

    dataset = Dataset.from_list(rows)

    result = evaluate(
        dataset=dataset,
        metrics=[
            faithfulness(),
            answer_relevancy(),
            context_precision(),
            context_recall(),
        ],
        embeddings=get_ragas_embeddings(),
    )

    print("\n📊 RAGAS Evaluation Results")
    print(result)


if __name__ == "__main__":
    run_evaluation()



# from ragas import evaluate
# from ragas.metrics.collections import (
#     faithfulness,
#     answer_relevancy,
#     context_precision,
#     context_recall
# )
# from datasets import Dataset

# from app.rag.pipeline import run_rag
# from evaluation.ragas_embeddings import get_ragas_embeddings


# def run_evaluation():
#     test_data = [
#         {"question": "What is RAG?", "ground_truth": "Retrieval Augmented Generation uses external documents."},
#         {"question": "What vector database is used?", "ground_truth": "Pinecone is used."},
#     ]

#     rows = []
#     for item in test_data:
#         result = run_rag(item["question"])

#         rows.append({
#             "question": item["question"],
#             "answer": result["answer"],
#             "contexts": result["contexts"],
#             "ground_truth": item["ground_truth"]
#         })

#     dataset = Dataset.from_list(rows)

#     result = evaluate(
#         dataset,
#         metrics=[
#             faithfulness,
#             answer_relevancy,
#             context_precision,
#             context_recall,
#         ],
#         embeddings=get_ragas_embeddings()
#     )

#     print("\n📊 RAGAS Evaluation Results")
#     print(result)


# if __name__ == "__main__":
#     run_evaluation()



# from ragas import evaluate
# from ragas.metrics import (
#     faithfulness,
#     answer_relevancy,
#     context_precision,
#     context_recall,
# )

# from evaluation.dataset import load_dataset
# from app.rag.pipeline import run_rag
#    # 👈 YOUR pipeline


# def run_evaluation():
#     dataset = load_dataset()
#     rows = []

#     for item in dataset:
#         result = run_rag(item["question"])


#         rows.append({
#             "question": item["question"],
#             "answer": result["answer"],
#             "contexts": result["contexts"],
#             "ground_truth": item["ground_truth"],
#         })

#     eval_dataset = dataset.from_list(rows)

#     scores = evaluate(
#         eval_dataset,
#         metrics=[
#             faithfulness,
#             answer_relevancy,
#             context_precision,
#             context_recall,
#         ],
#     )

#     print("\n📊 RAGAS Evaluation Results")
#     print(scores)


# if __name__ == "__main__":
#     run_evaluation()
