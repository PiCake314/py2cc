#include <print>
#include <string>

using namespace std::literals;


int main() {
	std::println("{}", 1 < 2 and 2 < 3);
	std::println("{}", 1 < 2 < 3);
	std::println("{}", 1 < (2 < 3));
	std::println("{}", 1 < 5 and 5 > 2 and 2 < 1);
	std::println("{}", 1 < 5 and 5 > 2 and 2 > 1);
}

