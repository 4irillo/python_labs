#include <bits/stdc++.h>
#include <string>
using namespace std;

class Int
{
 private:
    int value;
    bool correct;

 public:
    Int()
    {
        value = 0;
        correct = false;
    }
    Int(int _value)
    {
        value = _value;
        correct = true;
    }
    int getValue() const
    {
        return value;
    }
    bool isCorrect() const
    {
        return correct;
    }
};

ostream& operator<<(ostream& out, const Int& value)
{
    if (value.isCorrect())
    {
        out << value.getValue() << endl;
    }
    else
    {
        out << "error" << endl;
    }
    return out;
}

class Element
{
 public:
    int value;
    Element* next;

 public:
    Element(int _value, Element* _next)
    {
        value = _value;
        next = _next;
    }
    int getValue() const
    {
        return value;
    }
    Element* getNext() const
    {
        return next;
    }
    void setNext(Element* newNext)
    {
        next = newNext;
    }
};

class LinkedList
{
 private:
    Element* head;
    int size;

 public:
    LinkedList()
    {
        head = nullptr;
        size = 0;
    }
    ~LinkedList()
    {
        Element* currElement = head;
        while (currElement)
        {
            Element* tmp = currElement->getNext();
            delete currElement;
            currElement = tmp;
        }
    }

    Int insert(int number, int index)
    {
        if (index > size || index < 0)
        {
            return Int(-1e20);
        }
        Element* prevElement = head;
        for (int i = 0; i < index - 1; ++i)
        {
            prevElement = prevElement->getNext();
        }
        if (size != 0 && index != 0)
        {
            Element* newElem = new Element(number, prevElement->getNext());
            prevElement->setNext(newElem);
        }
        else
        {
            Element* newElem = new Element(number, head);
            head = newElem;
        }
        size++;
        return Int(number);
    }
    Int append(int number)
    {
        return insert(number, size);
    }
    Int prepend(int number)
    {
        return insert(number, 0);
    }
    Int deleteAt(int index)
    {
        if (index >= size || size == 0 || index < 0)
        {
            return Int();
        }
        int prevValue = 0;
        if (index != 0)
        {
            Element* prevElement = head;
            for (int i = 0; i < index - 1; ++i)
            {
                prevElement = prevElement->getNext();
            }
            Element* elem = prevElement->getNext();
            prevElement->setNext(elem->getNext());
            prevValue = elem->getValue();
            delete elem;
        }
        else
        {
            Element* elem = head;
            head = elem->getNext();
            prevValue = elem->getValue();
            delete elem;
        }
        size--;
        return Int(prevValue);
    }

    Int element(int index)
    {
        if (index >= size || size == 0 || index < 0)
        {
            return Int();
        }
        else
        {
            Element* elem = head;
            for (int i = 0; i < index; ++i)
            {
                elem = elem->getNext();
            }
            return Int(elem->getValue());
        }
    }

    int getSize()
    {
        return size;
    }
    void clear()
    {
        head = nullptr;
        size = 0;
    }
};

int main()
{
    LinkedList list;
    list.append(1);
    list.prepend(2);
    cout << "Size: " << list.getSize() << "\n";
    cout << "Element 0: " << list.element(0) << "\nElement 1: " << list.element(1) << "\n";
    list.deleteAt(0);
    cout << "Element 0 deleted\n";
    cout << "New size: " << list.getSize() << "\n";
    cout << "New element 0: " << list.element(0);
    return 0; 
}