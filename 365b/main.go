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

	if a <= 2 {
		Fprintln(out, a)
	} else {
		ans := 2
		tmp := 2
		for i := 2; i < a; i++ {
			if L[i] == L[i-1]+L[i-2] {
				tmp += 1
			} else {
				ans = max(ans, tmp)
				tmp = 2

			}
		}
		ans = max(ans, tmp)
		Fprintln(out, ans)
	}

}

func main() {
	run(os.Stdin, os.Stdout)
}
