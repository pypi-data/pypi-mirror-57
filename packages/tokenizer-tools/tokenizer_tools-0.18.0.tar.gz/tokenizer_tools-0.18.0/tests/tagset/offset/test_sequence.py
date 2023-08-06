from tokenizer_tools.tagset.offset.sequence import Sequence
from tokenizer_tools.tagset.offset.span import Span


def test_check_span_set():
    seq = Sequence("王小明在北京的清华大学读书。")
    seq.span_set.append(Span(0, 3, 'PERSON', ['王', '小', '明']))
    seq.span_set.append(Span(4, 6, 'GPE', ['北', '京']))
    seq.span_set.append(Span(7, 11, 'ORG', ['清', '华', '大', '学']))

    result, overlapped_result, mismatch_result = seq.check_span_set()
    assert result
    
    seq = Sequence("来一首蓝泽雨的歌。")
    seq.span_set.append(Span(3, 6, '歌手名', ['蓝', '泽', '雨']))
    seq.span_set.append(Span(5, 6, '歌曲名', '雨'))

    result, overlapped_result, mismatch_result = seq.check_span_set()
    assert not result


def test_eq_():
    a = Sequence("text")

    b = Sequence("text")

    assert a == b

    c = Sequence("other_text")

    assert a != c

    d = Sequence('text')
    d.span_set.append(Span(0, 1, 'entity'))

    e = Sequence('text')
    e.span_set.append(Span(0, 1, 'entity'))

    assert d == e

    f = Sequence('text')
    f.span_set.append(Span(0, 2, 'entity'))

    assert d != f
