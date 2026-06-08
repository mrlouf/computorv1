# ════════════════════════════════════════════════════════════
# ════════════════════════════════════════════════════════════

TARGET := computorv1

all: $(TARGET)

$(TARGET): cmd/main.go
	go build -o $@ cmd/main.go

clean:
	rm -f $(TARGET)
	rm -rf ./tmp
	rm -rf ./.logs

test: all
	cd test && ./test.sh

re: clean all

.PHONY: all clean re dev 