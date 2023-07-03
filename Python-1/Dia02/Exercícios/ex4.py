import json
import csv


def retrieve_books(file):
    return json.load(file)


def count_books_by_category(books):
    categories = {}
    for book in books:
        for category in book["categories"]:
            if not categories.get(category):
                categories[category] = 0
            categories[category] += 1
    return categories


def calculate_percentage_by_category(books_by_category, total_books):
    return [
        [category, num_books / total_books]
        for category, num_books in books_by_category.items()
    ]


def write_csv(file, header, rows):
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(rows)


if __name__ == "__main__":
    with open("Exercícios/arquivo.json") as file:
        books = retrieve_books(file)
    book_count_by_category = count_books_by_category(books)
    number_of_books = len(books)
    books_percentage_rows = calculate_percentage_by_category(
        book_count_by_category, number_of_books
    )
    header = ["categoria", "porcentagem"]
    with open("Exercícios/report.csv", "w") as file:
        write_csv(file, header, books_percentage_rows)
