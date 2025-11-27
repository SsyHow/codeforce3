package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
)

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
func solve(in *bufio.Reader, out *bufio.Writer) {
	var b int
	Fscan(in, &b)
	L := make([]int, b)
	for i := 0; i < b; i++ {
		Fscan(in, &L[i])
	}
	ans := -1
	for i := 1; i < b-1; i++ {
		if L[i] > L[i+1] && L[i] > L[i-1] {
			ans = 1
		}
		if L[i] < L[i+1] && L[i] < L[i-1] {
			ans = 1
		}
	}
	for i := 0; i < b-1; i++ {
		if abs(L[i]-L[i+1]) <= 1 {
			ans = 0
		}
	}
	Fprintln(out, ans)
}

func run(r io.Reader, w io.Writer) {
	in := bufio.NewReader(r)
	out := bufio.NewWriter(w)
	defer out.Flush()
	var a int
	Fscan(in, &a)
	for i := 0; i < a; i++ {
		solve(in, out)
	}

}

func main() {
	run(os.Stdin, os.Stdout)
}
