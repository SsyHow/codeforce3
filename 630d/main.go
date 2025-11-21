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
	var a int
	Fscan(in, &a)
	ans := 1
	for i := 0; i < a+1; i++ {
		ans += i * 6
	}
	Fprintln(out, ans)

}

func main() {
	run(os.Stdin, os.Stdout)
}
