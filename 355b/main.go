package main

import (
	"bufio"
	. "fmt"
	"io"
	"os"
)

func run(r io.Reader, w io.Writer) {
	in := bufio.NewReader(r)
	out := bufio.NewWriter(w)
	defer out.Flush()
	var c1, c2, c3, c4 int
	Fscan(in, &c1, &c2, &c3, &c4)
	var n, m int
	Fscan(in, &n, &m)

	L := make([]int, n)
	for i := 0; i < n; i++ {
		Fscan(in, &L[i])
	}
	M := make([]int, m)
	for i := 0; i < m; i++ {
		Fscan(in, &M[i])
	}

	k1 := 0
	for _, v := range L {
		k1 += min(v*c1, c2)
	}
	k1 = min(k1, c3)

	k2 := 0
	for _, v := range M {
		k2 += min(v*c1, c2)
	}
	k2 = min(k2, c3)
	Fprintln(out, min(k1+k2, c4))

}

func main() {
	run(os.Stdin, os.Stdout)
}
