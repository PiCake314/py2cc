#include <print>
#include <string>
#include <vector>
#include <ranges>

using namespace std::literals;


int main()
{
	auto i = 0;
	while (i < 10) {
		std::println("{}", i);
		i = i + 1;
	}
}


