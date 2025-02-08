#include <iostream>
#include <vector>
using namespace std;

class Node {
public:
    Node* next;
    int data;

    Node(int data1, Node* next1 = nullptr) {
        data = data1;
        next = next1;
    }
};

void printLinkedList(Node* head) {
    Node* current = head;
    while (current != nullptr) {
        cout << current->data << " ";
        current = current->next;
    }
    cout << endl;
}

int main() {
    vector<int> arr = {1, 2, 3, 4};
    Node* head = new Node(arr[0]);
    Node* current = head;

    for (int i = 1; i < arr.size(); ++i) {
        current->next = new Node(arr[i]);
        current = current->next;
    }

    printLinkedList(head);

    current = head;
    while (current != nullptr) {
        Node* next = current->next;
        delete current;
        current = next;
    }

    return 0;
}
