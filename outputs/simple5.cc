#include <print>
#include <string>
#include <vector>
#include <ranges>

using namespace std::literals;


int main()
{
	auto x = +10;
	auto y = -x;
	auto z = +x;
	auto a = true;
	auto b = not a;
	auto c = -1;
	auto d = ~c;
	std::println("{}", x);
	std::println("{}", y);
	std::println("{}", z);
	std::println("{}", a);
	std::println("{}", b);
	std::println("{}", c);
	std::println("{}", d);
}


