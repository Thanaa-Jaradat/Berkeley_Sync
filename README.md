# 🕒 Berkeley Clock Synchronization Simulation

This Python program simulates the **Berkeley Clock Synchronization Algorithm**, often used in distributed systems to synchronize clocks across nodes without relying on an external time source.

Each node in this simulation randomly generates a local clock value (integer), and a central daemon coordinates synchronization by averaging the offsets and instructing all clocks to update accordingly.

---

## 📌 Features

- Simulates 2 nodes + 1 daemon
- Randomized clock values
- Uses `multiprocessing` and `Pipe` for IPC (inter-process communication)
- Pure Python – no external libraries

---

## 🧠 How It Works

1. Each node generates a random "clock" value between 1 and 5.
2. The daemon sends its clock to each node.
3. Each node responds with its offset from the daemon.
4. The daemon calculates the **average offset** (including its own).
5. The daemon and nodes adjust their clocks based on the average.

This models **Berkeley's approach** of decentralized adjustment using a centralized coordinator.

---

## 🚀 Getting Started

### 1. Requirements
- Python 3.x

### 2. Run the simulation
```bash
python berkeley_sync.py
