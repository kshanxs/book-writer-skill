-- Turns the page-break marker in COMBINED.md into a real Word page break.

local WORD_PAGE_BREAK = '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'

function Div(el)
  local style = el.attributes.style or ''
  if #el.content == 0 and style:match('page%-break%-before:%s*always') then
    if FORMAT:match('docx') then
      return pandoc.RawBlock('openxml', WORD_PAGE_BREAK)
    end
    return {}
  end
end
