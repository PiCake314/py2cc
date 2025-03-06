#include <print>
#include <string>

using namespace std::literals;


int main() {
	auto i = 0;
	while (i < 10) {
		std::println("{}", i);
		i += 1;
	}
}

