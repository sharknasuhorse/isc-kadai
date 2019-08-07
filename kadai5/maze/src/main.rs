extern crate rand;

use rand::prelude::*;

fn main () {
    let n = 25;
    let mut maze = vec![vec!["wall"; n]; n];

    for i in 1..n-1{
        for j in 1..n-1 {
            maze[i][j] = "road";
        };
    }

    for i in 2..n-2{
        for j in 0..n-2 {
            if j % 2 == 0 && i%2 == 0 {
                maze[i][j] = "wall";
            };
        };
    }

    for i in 2..n-2 {
        for j in 1..n-1 {
            if &"wall" == &maze[i][j] && i%2 == 0 && j%2 == 0{
                // 0: Up, 1: Right, 2:Down, 3:Left
                //周りのあいてる場所を確認する

                let mut candidate_vec = Vec::new();

                if i == 2 {
                    candidate_vec.push(0)
                };

                if maze[i][j+1] == "road" {
                    candidate_vec.push(1)
                };

                if maze[i+1][j] == "road" {
                    candidate_vec.push(2)
                };

                if maze[i][j-1] == "road" {
                    candidate_vec.push(3)
                };


                //あいてる場所でrngをかける
                let mut rng = rand::thread_rng();
                let place = candidate_vec.iter().choose(&mut rng).unwrap();

                //wallにする
                match place {
                    0 => maze[i - 1][j] = "wall",
                    1 => maze[i][j+ 1] = "wall",
                    2 => maze[i + 1][j] = "wall",
                    3 => maze[i][j - 1] = "wall",
                    _ => println!("Error"),
                };
            };
        };
    };
    
    //Print
    for i in &maze {
        for j in i.iter() {
            if &"road" == j {
                print!("□");
            } else if &"wall" == j {
                print!("■");
            }
        };
        println!("");
    };





}
