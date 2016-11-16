close all;
logoName = 'starbucks';
frame_withlogo = 1;
for frame = 1:256
    
%     frame = 199;                                       %image frame
    try
        I = imread(['d:\logoDataSet\',logoName,'\',int2str(frame),'.jpg']);
    catch
        continue
    end
    h = figure(1);imshow(I);
    hold on;
    
    num = 1;                                         %number of cell
    
    while ~isempty(get(gcf,'CurrentAxes'))                      %the circulation end when the figure closed
        
        [temp,rect]=imcrop(I);                                  %choose the cell region manually
        rect = round(rect);
        try
            center = [rect(1)+0.5*rect(3), rect(2)+0.5*rect(4)];    %center of the rectangle
        catch
            continue
        end
        center = center';
        plot(center(1),center(2),'Marker','.','color','red');   %show the center point
        v1 = rect(1); v2 = rect(2); v3 = rect(3); v4 = rect(4); %show the rectangle u chose
        plot([v1,v1+v3],[v2,v2],[v1,v1],[v2,v2+v4],[v1,v1+v3],[v2+v4,v2+v4],[v1+v3,v1+v3],[v2,v2+v4],'LineWidth',2,'Color','r');
        
        ground_cell(frame_withlogo,num).temp = temp;                  %save pos image to Pos
        ground_cell(frame_withlogo,num).rect = rect;                  %save pos position to Pos
        ground_cell(frame_withlogo,num).name = logoName;
        ground_cell(frame_withlogo,num).num = frame;
        %imwrite(temp,strcat('maualresult\cell_',int2str(frame),'_',int2str(num),'.jpg'),'jpg');
        
        num = num + 1;
        pause;
    end
    try
        rect(1);
        frame_withlogo = frame_withlogo + 1;
    catch
        continue
    end
end
save(strcat('D:/logoDataSet/',logoName,'/',logoName),'ground_logo')