"""Write a portable Excel review workbook from saved sheet data; standard library only.
Usage: python3 scripts/review-workbook.py INPUT.json OUTPUT.xlsx
Never overwrite a manually annotated workbook: use a fresh output filename.
"""
import argparse,json,zipfile
from pathlib import Path
from xml.sax.saxutils import escape,quoteattr
p=argparse.ArgumentParser();p.add_argument('input',type=Path);p.add_argument('output',type=Path);a=p.parse_args()
if a.output.exists():p.error('Output exists; use a new filename to preserve review notes.')
data=json.loads(a.input.read_text());ns='http://schemas.openxmlformats.org/spreadsheetml/2006/main';rel='http://schemas.openxmlformats.org/officeDocument/2006/relationships'
def col(n):
 s=''
 while n:n,k=divmod(n-1,26);s=chr(65+k)+s
 return s
styles=f'''<styleSheet xmlns="{ns}"><fonts count="3"><font><sz val="11"/><name val="Calibri"/></font><font><b/><color rgb="FFFFFFFF"/><sz val="11"/><name val="Calibri"/></font><font><color rgb="FF0563C1"/><u/><sz val="11"/><name val="Calibri"/></font></fonts><fills count="3"><fill><patternFill patternType="none"/></fill><fill><patternFill patternType="gray125"/></fill><fill><patternFill patternType="solid"><fgColor rgb="FF024731"/><bgColor indexed="64"/></patternFill></fill></fills><borders count="1"><border/></borders><cellStyleXfs count="1"><xf/></cellStyleXfs><cellXfs count="3"><xf fontId="0" fillId="0" borderId="0" xfId="0" applyAlignment="1"><alignment vertical="top" wrapText="1"/></xf><xf fontId="1" fillId="2" borderId="0" xfId="0" applyAlignment="1"><alignment vertical="top" wrapText="1"/></xf><xf fontId="2" fillId="0" borderId="0" xfId="0" applyAlignment="1"><alignment vertical="top" wrapText="1"/></xf></cellXfs><cellStyles count="1"><cellStyle name="Normal" xfId="0" builtinId="0"/></cellStyles></styleSheet>'''
with zipfile.ZipFile(a.output,'w',zipfile.ZIP_DEFLATED) as z:
 types=['<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>','<Default Extension="xml" ContentType="application/xml"/>','<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>','<Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>']
 sheets=[];wrels=[]
 for i,sheet in enumerate(data['sheets'],1):
  name=sheet['name'];assert len(name)<=31 and not any(c in name for c in '[]:*?/\\');headers=sheet['headers'];rows=sheet['rows'];assert all(len(r)==len(headers) for r in rows)
  end=col(len(headers))+str(len(rows)+1);links=[];rels=[];xmlrows=[]
  for rownum,row in enumerate([headers]+rows,1):
   cells=[]
   for c,value in enumerate(row,1):
    value=str(value);ref=col(c)+str(rownum);style=1 if rownum==1 else 0
    if rownum>1 and value.startswith(('https://','http://')) and '\n' not in value:
     style=2;rid='rId'+str(len(rels)+1);rels.append(f'<Relationship Id="{rid}" Type="{rel}/hyperlink" Target={quoteattr(value)} TargetMode="External"/>');links.append(f'<hyperlink ref="{ref}" r:id="{rid}"/>')
    cells.append(f'<c r="{ref}" s="{style}" t="inlineStr"><is><t xml:space="preserve">{escape(value)}</t></is></c>')
   height=32 if rownum==1 else (64 if name!='Read Me' else 58)
   xmlrows.append(f'<row r="{rownum}" ht="{height}" customHeight="1">'+''.join(cells)+'</row>')
  cols=''.join(f'<col min="{j}" max="{j}" width="{w}" customWidth="1"/>' for j,w in enumerate(sheet['widths'],1))
  validation=''
  if name=='Page Review' and rows:validation=f'<dataValidations count="1"><dataValidation type="list" allowBlank="1" showErrorMessage="1" errorTitle="Choose a review status" error="Use the dropdown or add details in Your notes." sqref="A2:A{len(rows)+1}"><formula1>"Not reviewed,In progress,Done,Needs follow-up,Deferred"</formula1></dataValidation></dataValidations>'
  body=f'<worksheet xmlns="{ns}" xmlns:r="{rel}"><dimension ref="A1:{end}"/><sheetViews><sheetView workbookViewId="0"><pane xSplit="2" ySplit="1" topLeftCell="C2" activePane="bottomRight" state="frozen"/></sheetView></sheetViews><sheetFormatPr defaultRowHeight="18"/><cols>{cols}</cols><sheetData>'+''.join(xmlrows)+f'</sheetData><autoFilter ref="A1:{end}"/>'+validation+('<hyperlinks>'+''.join(links)+'</hyperlinks>' if links else '')+'<pageMargins left="0.3" right="0.3" top="0.5" bottom="0.5" header="0.2" footer="0.2"/></worksheet>'
  z.writestr(f'xl/worksheets/sheet{i}.xml',body)
  if rels:z.writestr(f'xl/worksheets/_rels/sheet{i}.xml.rels','<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'+''.join(rels)+'</Relationships>')
  sheets.append(f'<sheet name={quoteattr(name)} sheetId="{i}" r:id="rId{i}"/>');wrels.append(f'<Relationship Id="rId{i}" Type="{rel}/worksheet" Target="worksheets/sheet{i}.xml"/>');types.append(f'<Override PartName="/xl/worksheets/sheet{i}.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>')
 z.writestr('[Content_Types].xml','<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'+''.join(types)+'</Types>')
 z.writestr('_rels/.rels',f'<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="{rel}/officeDocument" Target="xl/workbook.xml"/></Relationships>')
 z.writestr('xl/workbook.xml',f'<workbook xmlns="{ns}" xmlns:r="{rel}"><sheets>'+''.join(sheets)+'</sheets></workbook>')
 wrels.append(f'<Relationship Id="styles" Type="{rel}/styles" Target="styles.xml"/>');z.writestr('xl/_rels/workbook.xml.rels','<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'+''.join(wrels)+'</Relationships>');z.writestr('xl/styles.xml',styles)
print(f'Created {a.output} ({len(data["sheets"])} sheets)')
