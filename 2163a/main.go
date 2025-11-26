package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
	"sort"
)

func solve(in *bufio.Reader, out *bufio.Writer) {
	var b int
	Fscan(in, &b)
	L := make([]int, b)
	for i := 0; i < b; i++ {
		Fscan(in, &L[i])
	}
	sort.Ints(L)

	for i := 1; i < b-1; i += 2 {
		if L[i] != L[i+1] {
			Fprintln(out, "NO")
			return
		}
	}
	Fprintln(out, "YES")
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
