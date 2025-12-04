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

	L := make([]int, b)
	for i := 0; i < b; i++ {
		Fscan(in, &L[i])
	}

	dp := make([][]int, 2)
	for i := 0; i < 2; i++ {
		dp[i] = make([]int, b+1)
	}

	for i := 1; i <= b; i++ {
		dp[i&1][L[i-1]] = max(dp[i&1][L[i-1]], dp[(i^1)&1][L[i-1]]+1)
	}
	for i := 1; i <= b; i++ {
		Fprint(out, max(dp[0][i], dp[1][i]), " ")
	}
	Fprintln(out)
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
