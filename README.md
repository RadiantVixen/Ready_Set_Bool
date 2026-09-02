# 🎛️ Ready_Set_Bool

An advanced interactive excursion into **Boolean Algebra**, **Propositional Logic**, **Conjunctive Normal Form (CNF)**, **SAT Solving**, **Set Theory**, and **Bijective Space-Filling Curves**. Designed to build a rigorous bottom-up understanding of how abstract logic maps to physical computation.

---

## 🎨 Visual Showcases & Conceptual Demos

This repository features custom high-fidelity visualizations explaining the core mathematical and hardware-level concepts implemented across the project.

### 1. Bitwise Full Adder Simulation (ex00)
*Visualizing arithmetic addition synthesized purely from gate-level operations (AND, XOR, and bitwise Left Shifts), bypassing the arithmetic `+` operator.*

![Bitwise Adder Simulation](https://lh3.googleusercontent.com/notebooklm/AKYWMX8GskvcIF-XB_7UFvN54_jEntkMtDArXAhCHcDZPt1ipaNkbO2SiN-vBDp2xp51FMN_wLNOgIFN4a4Rg4vS2v0SQDF8SRLEwxDbvv7IHv0lYRFS9G5UOphwCAUSBKEwjSuUitEAeDoLcQw5HUUe5HckbkmdNuA)

*   **XOR Gate (`^`)**: Computes the sum of bits without carries.
*   **AND Gate (`&`)**: Identifies position-wise carry generators.
*   **Left Shift (`<< 1`)**: Propagates carries to the next significant column for the subsequent iteration, continuing until all carries are resolved ($b = 0$).

---

### 2. Standard Binary vs. Gray Code Transitions (ex02)
*Why Gray Code is an engineering marvel. This visualization demonstrates the single-bit transition property of Gray Code compared to standard binary.*

![Gray Code Comparison](https://lh3.googleusercontent.com/notebooklm/AKYWMX-1eqv1D5DAZjhore2JG7wglR-8_WWZlRopXRTYoTUR69FJ8bFMFGe4k2pLfejz096x_cDNuzdFOsd0c2nQFXXEsWSttELFuoa2MVAKe82ui5wWKGmpxD6BGPS2y09TfYAP-aKXPZoIOmNDJwhISn5zUHt9zOQ)

*   **Standard Binary Glitches**: Moving from $7$ (`0111`) to $8$ (`1000`) forces **4 simultaneous bit flips**. In real-world physical systems (like optical rotary encoders), mechanical tolerances cause asynchronous reads, resulting in spurious intermediate states ("glitches").
*   **Gray Code Safety**: In Gray Code, moving between any consecutive integers (including wrap-around) guarantees that **exactly 1 bit changes**. This eliminates physical glitches and ensures absolute sensor stability.

---

### 3. Bijective Coordinate Normalization Curve (ex10 & ex11)
*Mapping a 2D integer coordinate grid $[0, 2^{16}-1]^2$ into a single-dimensional float interval $[0, 1]$ and reconstructively mapping it back with zero loss of dimensionality or bijection.*

![Coordinate Mapping Curve](https://lh3.googleusercontent.com/notebooklm/AKYWMX-XiBDrYQ8ALE2VldAy4v6TJ4wuRDsDMI0SlfheDeZ5EjQGKvi4g8B9o59Ef44O-OME-ni9q02UhjE7fZWr91oV81YpMZDqIO7i0MEqbiOopdlKrZsbiJXnj7kzlohgUEmlwuPde6DwskHVQDBp_3yjhUAObVI)

*   **Bitwise Concatenation**: Consolidates two 16-bit integers $X$ and $Y$ into a single 32-bit register by shifting $X$ left by 16 and applying a bitwise OR with $Y$.
*   **Normalization**: Scales the 32-bit integer $n \in [0, 2^{32}-1]$ down to a float $f \in [0, 1]$ via division by $(2^{32} - 1)$.
*   **Bijective Inverse**: Reconstructs the exact $(X, Y)$ coordinates from a floating point scalar $f$, preserving spatial tracking across 1D pipelines.

---

## 📂 Core Project Architecture

| Module | Purpose | Concepts Covered | Math / Algorithms |
|---|---|---|---|
| [**ex00**](./ex00/adder.py) | **Bitwise Adder** | Binary Half-Adder, carry prop | $a \oplus b$, $(a \wedge b) \ll 1$ loop |
| [**ex01**](./ex01/multiplier.py) | **Bitwise Multiplier** | Shift-and-Add multiplier | Gate-level logical multiplication |
| [**ex02**](./ex02/GrayCode.py) | **Gray Code** | Error-correcting codes, sensors | $g(x) = x \oplus (x \gg 1)$ |
| [**ex03**](./ex03/BooleanEvaluation.py) | **Boolean Evaluator** | RPN Evaluation, Postfix stack | Stack parsing, logical mappings |
| [**ex04**](./ex04/TruthTable.py) | **Truth Table Generator** | Combinatorial space generation | Recursive backtracking evaluation |
| [**ex05**](./ex05/NegationNormalForm.py) | **Negation Normal Form** | De Morgan's Laws, NNF AST | Recursive push of '!' to literals |
| [**ex06**](./ex06/ConjunctiveNormalForm.py) | **Conjunctive Normal Form** | Distributive Law of Logical OR | CNF Transformation, clause distribution |
| [**ex07**](./ex07/SAT.py) | **SAT Solver** | Boolean Satisfiability, NP-C | Brute-force backtracking search |
| [**ex08**](./ex08/Powerset.py) | **Powerset Generator** | Set theory, power sets | $2^N$ recursive subset expansion |
| [**ex09**](./ex09/SetEvaluation.py) | **Set Evaluator** | Boolean-Set Isomorphism | Logic ops $\rightarrow$ Union, Intersect, Comp |
| [**ex10**](./ex10/Curve.py) | **Bijection Curve** | 2D to 1D mapping, 32-bit registers | Bitwise shift-interleaving: $x \ll 16 \mid y$ |
| [**ex11**](./ex11/InverseFunction.py) | **Inverse Curve** | Floating point normalization | $n / (2^{32}-1)$ mapping & inverse |

---

## 🛠️ In-Depth Technical Deep Dives

### ex00 & ex01: Bitwise Arithmetic Synthesis
The arithmetic unit of a processor builds complex addition and multiplication entirely from gate logic.
*   **The Logic**: In `adder(a, b)`, standard addition is replaced by:
    ```python
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    ```
    Where XOR (`^`) acts as a half-adder sum, AND (`&`) represents the generated carry, and left-shift (`<< 1`) shifts the carry to the next binary column.

### ex03 & ex04: RPN & Combinatorial Truth Tables
Instead of standard infix strings (`A & B`), the repository parses postfix Reverse Polish Notation (`AB&`) to evaluate logical expressions efficiently. 
*   **RPN Evaluation**: Evaluates via a stack. Values are pushed. When an operator is encountered, operands are popped, evaluated, and the result is pushed back.
*   **Material Implication (`>`)**: A key logical operator. $B \implies A$ evaluates to $\neg B \vee A$. It is only false when the antecedent $B$ is true and the consequent $A$ is false.
*   **Equivalence (`=`)**: Evaluates as True if both operands possess matching truth values ($A \iff B$).

### ex05 & ex06: AST Parsing, NNF, and CNF Transformations
To convert propositional formulas into Conjunctive Normal Form (CNF), the code parses RPN into an Abstract Syntax Tree (AST), represented by a binary `node` structure, and runs structural simplifications:
1.  **Implication & Equivalence Elimination**:
    $$A \implies B \equiv \neg A \vee B$$
    $$A \iff B \equiv (A \wedge B) \vee (\neg A \wedge \neg B)$$
2.  **Negation Normal Form (NNF)**: Push all negations inward until they reside directly against literals, using De Morgan's Laws:
    $$\neg (A \wedge B) \equiv \neg A \vee \neg B$$
    $$\neg (A \vee B) \equiv \neg A \wedge \neg B$$
3.  **Conjunctive Normal Form (CNF)**: Recursively distribute logical OR (`|`) over logical AND (`&`):
    $$A \vee (B \wedge C) \equiv (A \vee B) \wedge (A \vee C)$$

### ex07: SAT Solving
The SAT solver determines if there exists some assignment of truth values to variables that makes the logical formula evaluate to True.
*   The solver parses the formula, extracts its unique literals, and recursively branches on truth assignments (backtracking search). If any branch resolves to True, the formula is satisfiable, otherwise unsatisfiable.

### ex08 & ex09: Set Algebra & Isomorphism
Underneath, set theory operations are completely isomorphic to boolean logic operations (Boolean Algebra). This module translates formula evaluations to operate directly on mathematical sets over a shared Universe:
*   **AND (`&`)** is mapped to **Intersection** ($A \cap B$)
*   **OR (`|`)** is mapped to **Union** ($A \cup B$)
*   **NOT (`!`)** is mapped to **Complement** ($U \setminus A$)
*   **XOR (`^`)** is mapped to **Symmetric Difference** ($A \Delta B$)

---

## 🚀 Getting Started

### Prerequisites
Make sure Python 3.10+ is installed on your environment.

### Running a Module
Each folder is fully executable and contains standard self-testing configurations:

```bash
# Run the Bitwise Adder Simulation
python3 ex00/adder.py

# Generate Truth Table for "AB&C|"
python3 ex04/TruthTable.py

# Convert "AB|C&!" to Negation Normal Form
python3 ex05/NegationNormalForm.py

# Test Boolean Satisfiability (SAT)
python3 ex07/SAT.py

# Run bijective coordinate mappings
python3 ex11/InverseFunction.py
```

### Technical Concepts Utilized
*   **Data Structures**: Abstract Syntax Trees (AST), postfix-order stacks.
*   **Recursion**: Recursive backtracking (SAT, Truth Tables), structural pattern matching (NNF, CNF distribution).
*   **Bit-Level Engineering**: Bit masking, bit shifts, bitwise arithmetic simulation.
*   **Mathematical Foundations**: Boolean algebra, propositional logic, bijective mappings, set theory.

---

*Authored with passion for machine learning, hardware optimization, and technical systems design.*
