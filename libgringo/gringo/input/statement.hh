// {{{ MIT License

// Copyright 2017 Roland Kaminski

// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to
// deal in the Software without restriction, including without limitation the
// rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
// sell copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:

// The above copyright notice and this permission notice shall be included in
// all copies or substantial portions of the Software.

// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
// FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
// IN THE SOFTWARE.

// }}}

#ifndef _GRINGO_INPUT_STATEMENT_HH
#define _GRINGO_INPUT_STATEMENT_HH

#include <gringo/terms.hh>
#include <gringo/input/types.hh>

namespace Gringo { namespace Input {

// {{{ declaration of Statement

class Statement : public Printable, public Locatable {
public:
    Statement(UHeadAggr &&head, UBodyAggrVec &&body);
    Statement(Statement const &other) = delete;
    Statement(Statement &&other) noexcept;
    Statement &operator=(Statement const &other) = delete;
    Statement &operator=(Statement &&other) noexcept;
    ~Statement() noexcept override;

    UStmVec unpool(bool beforeRewrite);
    bool hasPool(bool beforeRewrite) const;
    UStmVec unpoolComparison() const;
    void shift();
    bool hasUnpoolComparison() const;
    void assignLevels(VarTermBoundVec &bound);
    bool simplify(Projections &project, Logger &log);
    void rewrite();
    Symbol isEDB() const;
    void print(std::ostream &out) const override;
    void check(Logger &log) const;
    void replace(Defines &dx);
    void toGround(ToGroundArg &x, Ground::UStmVec &stms) const;
    void add(ULit &&lit);
    void initTheory(TheoryDefs &def, Logger &log);

private:
    UHeadAggr     head_;
    UBodyAggrVec  body_;
};

// }}}

} } // namespace Input Gringo

#endif // _GRINGO_INPUT_STATEMENT_HH
