use std::io;

fn main() {
    let mut marks = Vec::new();
    let mut input = String::new();

    println!("Enter marks of 5 subjects (out of 100):");

    for i in 1..=5 {
        input.clear();
        println!("Subject {}:", i);
        io::stdin().read_line(&mut input).expect("Failed to read");
        let value: f32 = input.trim().parse().expect("Enter a number");
        marks.push(value);
    }

    let total: f32 = marks.iter().sum();
    let percentage = (total / 500.0) * 100.0;

    println!("Total Marks = {}", total);
    println!("Percentage = {:.2}%", percentage);
}

