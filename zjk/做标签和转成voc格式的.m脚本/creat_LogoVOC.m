function creat_LogoVOC(logoName,path)
%#logoName为每类logo图片文件夹的名字与savePOSregion.m生成.mat文件的名字
    %load(strcat('D:\logoDataSet\',logoName,'\',logoName,'.mat'))
    load(strcat(path,logoName,'\',logoName,'.mat'))
    for i = 1:length(ground_cell)
        rec_logo.annotation.folder = 'logo2016';
        rec_logo.annotation.filename = sprintf('%06d',ground_cell(i,1).num);
        rec_logo.annotation.source.database = 'logo2016_open_image';
        rec_logo.annotation.source.annotation = 'SX_2016';
        rec_logo.annotation.source.image = 'open_image';
        rec_logo.annotation.source.flckrid = '0';
        rec_logo.annotation.owner.flckrid = 'ZZH';
        rec_logo.annotation.owner.name = 'SXWL';
        rec_logo.annotation.size.width = '0';%尺寸还没读
        rec_logo.annotation.size.height = '0';
        rec_logo.annotation.size.depth = '3';
        rec_logo.annotation.segmented = '0';
        j = 1;
        while(~isempty(ground_cell(i,j).rect()))
            rec_logo.annotation.object(j).name = ground_cell(i,j).name
            rec_logo.annotation.object(j).pose = 'no'
            rec_logo.annotation.object(j).truncated = 0
            rec_logo.annotation.object(j).difficult = 0
            rec_logo.annotation.object(j).bndbox.xmin = ground_cell(i,j).rect(1);
            rec_logo.annotation.object(j).bndbox.ymin = ground_cell(i,j).rect(2);
            rec_logo.annotation.object(j).bndbox.xmax = ground_cell(i,j).rect(1)+ground_cell(i,j).rect(3);
            rec_logo.annotation.object(j).bndbox.ymax = ground_cell(i,j).rect(2)+ground_cell(i,j).rect(4);
            j = j+1;
            try 
                ground_cell(i,j+1);
            catch
                break
            end
        end
        VOCwritexml(rec_logo,strcat(path,'annotation\',rec_logo.annotation.filename,'.xml'))
        clear rec_logo
    end
end
        