package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	"slices"
)

func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func run(r io.Reader, w io.Writer) {
	in := bufio.NewReader(r)
	out := bufio.NewWriter(w)
	defer out.Flush()
	var a int
	Fscan(in, &a)
	L := make([]int, a/2)
	for i := 0; i < a/2; i++ {
		Fscan(in, &L[i])
	}
	slices.Sort(L)
	ans1 := 0
	ans2 := 0

	for i := 0; i < a/2; i++ {
		ans1 += Abs(L[i] - (2*i + 1))
	}
	for i := 0; i < a/2; i++ {
		ans2 += Abs(L[i] - (2*i + 2))
	}
	Fprintln(out, min(ans1, ans2))

}

func main() {
	run(os.Stdin, os.Stdout)
}
