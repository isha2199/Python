import express from "express";


const app = express();
app.use(express.json());
const PORT = 3000;

let problems = [
    {
        id: 0,
        title: "Two Sum",
        difficulty: "Easy",
        description: "Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.",
    },
    {
        id: 1,
        title: "Add Two Numbers",
        difficulty: "Medium",
        description: "You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.",
    }
];

app.get("/api/problems", (req,res)=>{
    res.json(problems);
});

app.post("/api/problems", (req,res)=>{
    const body = req.body;
    problems = [
        ...problems,
        body
    ]
    res.json(problems);
})

app.put("/api/problems/:id", (req,res)=>{
    const body = req.body;
    const id = req.params.id;
    problems = problems.map((p) => {
        if(p.id == id){
            return { id, ...body }
        }
        return p;
    })
    return res.json(problems);
})

app.delete("/api/problems/:id", (req,res)=>{
    const body = req.body;
    const id = req.params.id;
    problems = problems.filter((p) => p.id != id);
    res.json(problems);
})

app.patch("/api/problems/:id", (req,res)=>{
    const body = req.body;
    const id = req.params.id;
    const problem = problems.find((p) => p.id == id);
    problems = problems.map((p) => {
        if(p.id == id){
            return { ...problem, ...body }
        }
        return p;
    })
    return res.json(problems);
})


app.listen(PORT, () => {
    console.log(`Server is up and running on port ${PORT}`);
})