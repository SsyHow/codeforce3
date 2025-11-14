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
	var a int
	Fscan(in, &a)
	L := make([]int, a)

	for i := 0; i < a; i++ {
		Fscan(in, &L[i])
	}
	var ans int
	for idx, v := range L {
		ans += (v-1)*(idx+1) + 1
	}
	Fprintln(out, ans)
}

func main() {
	run(os.Stdin, os.Stdout)
}
