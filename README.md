# FCFS Scheduling Algorithm in Python

This project implements the **First Come First Serve (FCFS)** CPU scheduling algorithm using Python.  
It simulates how processes are executed based on their arrival time and calculates:

- Completion Time
- Turnaround Time
- Waiting Time

---

## 📌 What is FCFS?

FCFS (First Come First Serve) is a non-preemptive scheduling algorithm where the process that arrives first gets executed first — just like a queue.

---

## 🧠 Input Format

Each process is written as:

[arrival_time, burst_time, process_id]

---

### Example:

process_list = [
    [2, 6, "p1"],
    [5, 2, "p2"],
    [1, 8, "p3"],
    [0, 3, "p4"],
    [4, 4, "p5"]
]

---

## 📊 Output Example

['p4', 'p3', 'p1', 'p5', 'p2']
{'p4': [3, 3, 0], 'p3': [11, 10, 2], 'p1': [17, 15, 9], 'p5': [21, 17, 13], 'p2': [23, 18, 16]}

---

## 📚 References
- Hallow Teaches Stuff: https://youtu.be/TH_vRsr5Dy8?si=IDET4Du4dyjxescL

---

## 🖼 Images
![FCFS Output](Output.png)

---
