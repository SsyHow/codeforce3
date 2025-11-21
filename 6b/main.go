package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
)

func solve(in *bufio.Reader, out *bufio.Writer) {
	var b int
	Fscan(in, &b)
}

func run(r io.Reader, w io.Writer) {
	in := bufio.NewReader(r)
	out := bufio.NewWriter(w)
	defer out.Flush()
	var a, b int
	var c string
	Fscan(in, &a, &b)
	Fscan(in, &c)
	s := rune(c[0])

	//Fprintln(out, a, b, s)
	L := make([][]rune, a)
	for i := 0; i < a; i++ {
		var t string
		Fscan(in, &t)
		//Fprintln(out, t)
		L[i] = []rune(t)
	}

	x := make(map[rune]int)
	for i := 0; i < a; i++ {
		for j := 0; j < b; j++ {
			if L[i][j] == s {
				if i > 0 && L[i-1][j] != s && L[i-1][j] != '.' {
					x[L[i-1][j]] += 1
				}
				if i < a-1 && L[i+1][j] != s && L[i+1][j] != '.' {
					x[L[i+1][j]] += 1
				}
				if j > 0 && L[i][j-1] != s && L[i][j-1] != '.' {
					x[L[i][j-1]] += 1
				}
				if j < b-1 && L[i][j+1] != s && L[i][j+1] != '.' {
					x[L[i][j+1]] += 1
				}
			}
		}
	}
	Fprintln(out, len(x))

}

func main() {
	run(os.Stdin, os.Stdout)
}
