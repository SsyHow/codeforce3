package main

import (
	"bufio"
	. "fmt"
	"os"
)

func run() {
	inFile, _ := os.Open("input.txt")
	outFile, _ := os.Create("output.txt")
	in := bufio.NewReader(inFile)
	out := bufio.NewWriter(outFile)
	defer out.Flush()
	var a, b int
	Fscan(in, &a, &b)

	if a >= b {
		for i := 0; i < b; i++ {
			Fprint(out, "BG")
		}
		for i := 0; i < a-b; i++ {
			Fprint(out, "B")
		}
	} else {
		for i := 0; i < a; i++ {
			Fprint(out, "GB")
		}
		for i := 0; i < b-a; i++ {
			Fprint(out, "G")
		}
	}
}

func main() {
	run()
}
